import ast
import csv
import os
from os import listdir
from os.path import join
from pprint import pprint

from cnn_architecture_detector import is_unet
from common import get_repo_full_name_and_repo_file_path
from find_definition import FindDefinition
from non_expanding_feature_map_smelled_file import NonExpandingFeatureMapSmelledFile
from smelled_file import SmelledFile, SmellType


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


def detect_non_expanding_feature_map(repo_name, file_name, file_path):
    code_ast = get_ast(file_path)
    call_groups = get_conv2d_calls_in_groups(code_ast)

    smelled_lines = list()
    for calls in call_groups:
        for i in range(len(calls) - 1):
            if calls[i].filters_value > calls[i + 1].filters_value:
                if is_unet(calls):
                    print(
                        f"--------------Detected U-Net model in {os.path.join(repo_name, file_name)} from line {calls[0].line_no} to {calls[-1].line_no}")
                    break
                else:
                    smelled_lines.append(NonExpandingFeatureMapSmelledFile(repo_name, file_name, calls[i + 1].line_no, calls[i].filters_value))
    return smelled_lines


if __name__ == '__main__':
    directory = "data/repo_files"
    files = listdir(directory)

    error_count = 0
    detection_count = 0

    repo_list = list()
    for i in range(len(files)):
        file = files[i]
        path = join(directory, file)
        print(f"[{i+1}] Processing file {path}")

        repo_name, file_name = get_repo_full_name_and_repo_file_path(file)

        try:
            detected_lines = detect_non_expanding_feature_map(repo_name, file_name, path)
            if len(detected_lines) > 0:
                detection_count += 1
                for line in detected_lines:
                    repo_list.append(line)
        except Exception as e:
            error_count += 1
            print(f"Error: {e}")
            continue

    print(f"Couldn't process {error_count} files")
    print(f"Found {detection_count} files having non-expanding feature map")
    pprint(repo_list)

    with open("data/repositories_with_smells/non_expanding_feature_maps/repo_list.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Full Name", "File Name", "Line No."])
        for repo in repo_list:
            writer.writerow(repo.get_row())