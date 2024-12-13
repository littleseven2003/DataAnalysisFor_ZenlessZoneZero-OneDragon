# -*- coding: utf-8 -*-

"""
GetData.py
Author: 筱柒_littleseven
Github: https://github.com/littleseven2003
"""

import git
import os
import pandas
import re

class RepoManager:
    def __init__(self, repo_url, local_path='./repo', local_mirror_path='./mirror_repo'):
        self.repo_url = repo_url
        self.local_path = local_path
        self.local_mirror_path = local_mirror_path

    def clone_repo(self):
        # 克隆主仓库
        self._clone_main_repo()

        # 克隆镜像仓库
        self._clone_mirror_repo()

    def _clone_main_repo(self):
        # 检查主仓库是否已经存在
        if not os.path.exists(self.local_path):
            print(f"Cloning main repository from {self.repo_url}...")
            repo = git.Repo.clone_from(self.repo_url, self.local_path, no_single_branch=True)
            repo.git.fetch('--all')
        else:
            print("Main repository already exists, no need to clone.")

    def _clone_mirror_repo(self):
        # 检查镜像仓库是否已经存在
        if not os.path.exists(self.local_mirror_path):
            print(f"Cloning mirror repository from {self.repo_url}...")
            repo = git.Repo.clone_from(self.repo_url, self.local_mirror_path, mirror=True)
        else:
            print("Mirror repository already exists, no need to clone.")


class Commits:
    def __init__(self, local_path='./repo', local_mirror_path='./mirror_repo'):
        self.local_path = local_path
        self.local_mirror_path = local_mirror_path

    def get_commit_data(self, branch='main'):
        repo = git.Repo(self.local_mirror_path)
        commits = list(repo.iter_commits(branch))

        commit_data = []
        for commit in commits:
            commit_data.append({'date': commit.committed_datetime,
                                'message': commit.message,
                                'category': None,
                                'author': commit.author.name,
                                })
        df = pandas.DataFrame(commit_data)
        df['date'] = pandas.to_datetime(df['date'], utc=True)
        df.set_index('date', inplace=True)

        return df

    def categorize_commits(self, df):
        self.df = df.copy()
        # 使用正则表达式或其他方法对提交信息进行分类
        self.df['category'] = 'Other'  # 默认类别

        # 定义正则表达式
        bug_pattern = re.compile(r'(修复|bug)', re.IGNORECASE)
        feature_pattern = re.compile(r'(新增|加入|增加)', re.IGNORECASE)
        testing_pattern = re.compile(r'(测试)', re.IGNORECASE)
        logging_pattern = re.compile(r'(日志)', re.IGNORECASE)
        optimization_pattern = re.compile(r'(优化|界面|UI|延长|调整|改进|提升)', re.IGNORECASE)

        # 根据正则表达式分类
        self.df.loc[self.df['message'].str.contains(bug_pattern), 'category'] = 'Bug Fix'
        self.df.loc[self.df['message'].str.contains(feature_pattern), 'category'] = 'New Feature'
        self.df.loc[self.df['message'].str.contains(testing_pattern), 'category'] = 'Testing'
        self.df.loc[self.df['message'].str.contains(logging_pattern), 'category'] = 'Logging'
        self.df.loc[self.df['message'].str.contains(optimization_pattern), 'category'] = 'Optimization'

        return self.df

if __name__ == "__main__":
    # Your main code logic goes here
    print("Hello from GetData.py!")

    # Example usage:
    # You can call functions from other modules here
    # from my_module import my_function
    # my_function()