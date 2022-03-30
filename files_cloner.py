import datetime
import math
import os
import time
from pprint import pprint

import requests
from github import Github
from github.GithubException import RateLimitExceededException
from github.GithubObject import GithubObject
from github.PaginatedList import PaginatedList

ACCESS_TOKEN = "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" # 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
PAGE_SIZE = 100
g = Github(ACCESS_TOKEN, per_page=PAGE_SIZE)


def wait():
    rate = g.get_rate_limit().search
    reset_utc_timestamp = rate.reset.timestamp()
    now_utc_timestamp = datetime.datetime.utcnow().timestamp()
    sleep_time = (reset_utc_timestamp - now_utc_timestamp) + 5  # 5s buffer time
    print(f"Waiting {sleep_time}s to pass rate limit")
    time.sleep(sleep_time)


def get_filename(file: GithubObject):
    filename = os.path.join(file.repository.full_name, file.path)
    filename = filename.replace('/', '$')
    return filename.replace('\\', '$')


def save_file(url: str, filename: str, count: int):
    r = requests.get(url, allow_redirects=True)

    directory = "data/repo_files/"
    if not os.path.exists(directory):
        print("Path doesn't exists")
        os.mkdir(directory)
    full_path = os.path.join(directory, filename)

    print(f"[{count}] Saving {full_path}")
    open(full_path, 'wb').write(r.content)


def clone_files_by_page(query, page_index):
    try:
        return g.search_code(query).get_page(page_index)
    except RateLimitExceededException as e:
        wait()
        return clone_files_by_page(query, page_index)


def clone_files():
    query = "Conv2D keras in:file extension:py language:python size:1201..1300"

    count = 0
    for page_index in range(10): # Allows to query 10 pages
        page_codes = clone_files_by_page(query, page_index)
        print(f"{len(page_codes)} results in page {page_index + 1}")

        for code in page_codes:
            count += 1
            save_file(code.download_url, get_filename(code), count)


if __name__ == '__main__':
    clone_files()