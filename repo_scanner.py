import glob
import os

from non_expanding_feature_map_detector import detect_non_expanding_feature_map


def scan_repo(repo_full_name):
    repo_path = os.path.join("data/repositories_with_smells/non_expanding_feature_maps/", repo_full_name.replace('/', '$'))
    files = glob.glob(repo_path + '/**/*.py', recursive=True)
    for file in files:
        file_name = "/".join(file.split('\\')[1:])
        try:
            detected_lines = detect_non_expanding_feature_map(repo_full_name, file_name, file)
            if len(detected_lines) > 0:
                for detected_line in detected_lines:
                    print(f"Found non-expanding feature map in file {file_name} line {detected_line.smell_line_no}")
        except Exception as e:
            continue


if __name__ == '__main__':
    scan_repo("abcsFrederick/yliu_utilities")