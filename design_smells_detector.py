import glob
import os, sys

from non_expanding_feature_map_detector import detect_non_expanding_feature_map
from non_representative_statistics_estimation_detection import *


def detect_nrse_in_project(repo_full_name, repo_path):
    df_nrse_info = NRSE_detection(repo_path)
    print("Non Representative Statistical Estimation Found", len(df_nrse_info.index))
    print("Project Containing Non Representative Statistical Estimation", df_nrse_info['Filename'].nunique())

    print (df_nrse_info)

    df_nrse_info.to_csv("NRSE_detect.csv", encoding='utf-8', index=False)


def detect_nfm_in_project(repo_full_name, repo_path):
    files = glob.glob(repo_path + '/**/*.py', recursive=True)
    for file in files:
        file_name = "/".join(file.split('\\')[1:])
        try:
            detected_lines = detect_non_expanding_feature_map(repo_full_name, file_name, file)
            if len(detected_lines) > 0:
                print(f"--------------------{repo_full_name}--------------------")
                with open(file, newline='') as py_file:
                    lines = py_file.readlines()
                for detected_line in detected_lines:
                    line = lines[detected_line.smell_line_no-1].rstrip()
                    print(f"Found non-expanding feature map in file \"{file_name}\" line {detected_line.smell_line_no}")
                    print(f"--> {line}")
                    print(f"Set the 1st parameter of Conv2D to {detected_line.previous_filters_value*2} instead of {detected_line.previous_filters_value}")
                    print("\n")
                print(f"----------------------------------------------------------------")
        except Exception as e:
            continue


def main():
    args = sys.argv[1:]

    if len(args) < 2:
        print("Please follow the argument style e.g. python3 design_smells_detector.py <smell_code> <project_path>")
        return

    code = args[0]
    repo_path = args[1]

    if code == 'nfm':
        print("Working for the detection of NFM in project: ", repo_path)
        detect_nfm_in_project("", repo_path)


    elif code == 'nrse':
        print("Working for NRSE Design Smell on Project Path: ", repo_path)
        detect_nrse_in_project("", repo_path)


if __name__ == '__main__':
