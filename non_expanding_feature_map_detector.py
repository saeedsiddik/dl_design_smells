import ast
import os
from os import listdir
from os.path import isfile, join
from pprint import pprint

from find_definition import FindDefinition


def get_ast(file_path):
    # file = open('data/smell_sample/non_expanding_feature_maps/nefm_1.py', 'r')
    # file = open('data/non_smell_sample/1.py', 'r')
    # file = open('data/smell_sample/non_expanding_feature_maps/googlenet.py', 'r')
    file = open(file_path, 'r')
    return ast.parse(file.read())


def get_conv2d_calls_in_groups(code_ast):
    fd = FindDefinition()
    fd.visit(code_ast)
    return fd.results


def detect_non_expanding_feature_map(file_path):
    detection_lineno = []
    code_ast = get_ast(file_path)
    call_groups = get_conv2d_calls_in_groups(code_ast)

    for calls in call_groups:
        for i in range(len(calls) - 1):
            if calls[i].filters_value > calls[i + 1].filters_value:
                detection_lineno.append(calls[i + 1].line_no)
    return detection_lineno


if __name__ == '__main__':
    directory = "data/repo_files"
    files = listdir(directory)
    error_count = 0
    detection_count = 0
    for i in range(len(files)):
        file = files[i]
        path = join(directory, file)
        print(f"[{i}] Processing file {path}")
        try:
            detection_lineno = detect_non_expanding_feature_map(path)
            if len(detection_lineno) > 0:
                detection_count += 1
                print(f"Non-expanding feature map found in line no: {detection_lineno}")
        except Exception as e:
            error_count += 1
            print(f"Error: {e}")
            continue
    print(f"Couldn't process {error_count} files")
    print(f"Total {detection_count} files have non-expanding feature map smell")