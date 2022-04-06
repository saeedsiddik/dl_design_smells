import glob
import os

from non_expanding_feature_map_detector import detect_non_expanding_feature_map


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


if __name__ == '__main__':
    repo_full_name = "abcsFrederick/yliu_utilities"
    repo_path = os.path.join("data/repositories_with_smells/non_expanding_feature_maps/", repo_full_name.replace('/', '$'))
    detect_nfm_in_project(repo_full_name, repo_path)