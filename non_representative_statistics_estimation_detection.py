import re
import glob, os
import pandas as pd
from fnmatch import fnmatch
from pprint import pprint
from datetime import datetime

import ast
from ast import NodeVisitor, literal_eval

from find_batch_dropout_call import FindBatchNormDropoutCall

def get_list_of_filename(root, extension):
    target_filenames_list = []

    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, extension):
                target_filenames_list.append(os.path.join(path, name))

    print ("Total files: ", (len(target_filenames_list)))
    return target_filenames_list

def filter_py_file_after_preprocess(list_of_py_files):
    method_names = ["BatchNormalization", "Dropout"]

    list_of_ast_filenames = []
    list_of_ast_method_dict = []
    list_of_ast_trees = []

    for file_name in list_of_py_files:
        try:
            file = open(file_name, 'r')
            ast_data = ast.parse(file.read())

            intra_file_ast_method_dict = []
            atleast_one_methods_used = True

            for method_name in method_names:
                fc = FindBatchNormDropoutCall(method_name)
                fc.visit(ast_data)
                # print (fc.result.keys())
                # print (("Keys %s: Values %s, Len %s")%(fc.result.keys(), fc.result.values(), len(fc.result.values() ) ))

                atleast_one_methods_used = bool([a for a in fc.result.values() if a != []])

                intra_file_ast_method_dict.append(fc.result)

            if(atleast_one_methods_used):
                list_of_ast_filenames.append(file_name)
                list_of_ast_method_dict.append(intra_file_ast_method_dict)
                list_of_ast_trees.append(ast_data)


        except Exception as e:
            with open("error_log.txt", 'a') as log_file:
                now_time  = datetime.now()
                log_file.write("Problem in AST: Filename " + file_name + ":  " + str(e) + '\n')

    print ('Total prepared Projects: ', len(list_of_ast_filenames))
    
    return (list_of_ast_filenames, list_of_ast_method_dict, list_of_ast_trees)

def get_function_info(filename, code_tree):
    filename_list, function_name, start_line, end_line = [], [], [], []
    for node in ast.walk(code_tree):
        if isinstance(node, ast.FunctionDef):
            filename_list.append(filename)
            function_name.append(node.name)
            start_line.append(node.lineno)
            end_line.append(node.end_lineno)
            
            # print (node.name, node.lineno, node.end_lineno)
    data = {'Filename':filename_list, 'FunctionName':function_name, 'StartLine': start_line, 'EndLine':end_line}
    df_function_info = pd.DataFrame(data)
    return df_function_info       

def NRSE_detection():
    filenmaes_list, function_names_list, bacthnorm_line_list, dropout_line_list = [], [], [], []
    
    list_of_py_files = get_list_of_filename("data/", "*.py")
    
    list_of_ast_filenames, list_of_ast_method_dict, list_of_ast_trees = filter_py_file_after_preprocess(list_of_py_files)
    
    for file_wise_method_line, ast_filename, ast_tree in zip(list_of_ast_method_dict, list_of_ast_filenames, list_of_ast_trees):

        batchNormal_lines, dropout_lines = file_wise_method_line[0].get('BatchNormalization'), file_wise_method_line[1].get('Dropout')
        df_function_info = get_function_info(ast_filename, ast_tree)


        for index, row in df_function_info.iterrows():
            # print(row['FunctionName'], row['StartLine'], row['EndLine'])
            batchNormal_lines_within_a_function, dropout_lines_within_a_function = [], []

            for batch_line in batchNormal_lines:
                if(( batch_line[0] > row['StartLine']) and ( batch_line[0] < row['EndLine'])):
                    batchNormal_lines_within_a_function.append(batch_line[0])

            for dropout_line in dropout_lines:
                if(( dropout_line[0] > row['StartLine']) and ( dropout_line[0] < row['EndLine'])):
                    dropout_lines_within_a_function.append(dropout_line[0])

            for index in range(min(len(batchNormal_lines_within_a_function), len(dropout_lines_within_a_function))):
                if(batchNormal_lines_within_a_function[index] > dropout_lines_within_a_function[index]):
                    filenmaes_list.append(ast_filename) 
                    function_names_list.append(row['FunctionName'])
                    bacthnorm_line_list.append(batchNormal_lines_within_a_function[index])
                    dropout_line_list.append(dropout_lines_within_a_function[index])

    data = {'Filename':filenmaes_list, 'FunctionName':function_names_list, 'BatchNorm_Lineno': bacthnorm_line_list, 'Dropout_Lineno':dropout_line_list}
    df_nrse_info = pd.DataFrame(data)
    return df_nrse_info  

def main():
    df_nrse_info = NRSE_detection()
    print("Non Representative Statistical Estimation Found", len(df_nrse_info.index))
    print("Project Containing Non Representative Statistical Estimation", df_nrse_info['Filename'].nunique())
    
    df_nrse_info.to_csv("NRSE_detect.csv", encoding='utf-8', index=False)
   

if __name__ == "__main__":
    main()
    
