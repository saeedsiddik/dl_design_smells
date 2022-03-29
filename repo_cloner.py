import csv
import os.path

import git
import pandas as pd
from git import Repo


class CloneProgress(git.remote.RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        print(self._cur_line)


def clone(github_page, destination_path):
    Repo.clone_from(github_page, destination_path, progress=CloneProgress())


def pull(repo_path):
    print(f'Pulling {repo_path}')
    try:
        repo = git.Repo(repo_path)
        repo.remotes.origin.pull()
    except:
        pass


def clone_repositories():
    repo_names = set()
    with open("data/repositories_with_smells/non_expanding_feature_maps/repo_list.csv", 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        for row in reader:
            repo_names.add(row[0])

    for idx, full_name in enumerate(repo_names):
        github_page = "https://github.com/" + full_name
        destination_path = "data/repositories_with_smells/non_expanding_feature_maps/" + full_name.replace('/', '$')

        try:
            print(f"[{idx+1}] Cloning {github_page}")
            clone(github_page, destination_path)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    clone_repositories()