import os

from common import get_repo_full_name_and_repo_file_path


def get_repos():
    path = "data/repo_files/"
    repos = set()
    for file in os.listdir(path):
        repo_name, file_path = get_repo_full_name_and_repo_file_path(file)
        print(repo_name)
        repos.add(repo_name)
    print(len(repos))
    return repos


if __name__ == '__main__':
    get_repos()