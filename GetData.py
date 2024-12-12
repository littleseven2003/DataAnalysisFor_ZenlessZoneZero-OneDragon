# -*- coding: utf-8 -*-

"""
GetData.py
Author: 筱柒_littleseven
Github: https://github.com/littleseven2003
"""

import git
import os
import pandas

class RepoManager:
    def __init__(self, repo_url, local_path='./repo'):
        self.repo_url = repo_url
        self.local_path = local_path

    def clone_repo(self):
        # 检查仓库是否已经存在
        if not os.path.exists(self.local_path):
            print(f"Cloning repository from {self.repo_url}...")
            git.Repo.clone_from(self.repo_url, self.local_path, mirror=True)
        else:
            print("Repository already exists, no need to clone.")


class Commits:
    def __init__(self, local_path='./repo'):
        self.local_path = local_path

    def get_commit_data(self, branch='main'):
        # 打开现有的Git仓库
        repo = git.Repo(self.local_path)

        # 提取提交历史
        commits = list(repo.iter_commits(branch))
        commit_dates = [commit.committed_datetime for commit in commits]

        # 转换为DataFrame
        df = pandas.DataFrame(commit_dates, columns=['date'])
        df['date'] = pandas.to_datetime(df['date'], utc=True)
        df.set_index('date', inplace=True)

        return df

if __name__ == "__main__":
    # Your main code logic goes here
    print("Hello from GetData.py!")

    # Example usage:
    # You can call functions from other modules here
    # from my_module import my_function
    # my_function()