# -*- coding: utf-8 -*-

"""
GetData.py
Author: 筱柒_littleseven
Github: https://github.com/littleseven2003
"""

import git
import os
import pandas as pd

class RepoManager:
    def __init__(self, repo_url, local_path='./repo'):
        self.repo_url = repo_url
        self.local_path = local_path

    def clone_repo(self):
        # 检查仓库是否已经存在
        if not os.path.exists(self.local_path):
            print(f"Cloning repository from {self.repo_url}...")
            git.Repo.clone_from(self.repo_url, self.local_path)
        else:
            print("Repository already exists, no need to clone.")


if __name__ == "__main__":
    # Your main code logic goes here
    print("Hello from GetData.py!")

    # Example usage:
    # You can call functions from other modules here
    # from my_module import my_function
    # my_function()