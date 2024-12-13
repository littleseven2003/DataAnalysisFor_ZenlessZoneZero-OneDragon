# -*- coding: utf-8 -*-

"""
Main.py
Author: 筱柒_littleseven
Github: https://github.com/littleseven2003
"""

import matplotlib.pyplot as plt
from GetData import RepoManager, Commits

REPO_URL = 'https://github.com/DoctorReid/ZenlessZoneZero-OneDragon'

class Visualizer:
    def __init__(self):
        pass
    def visualize_commit_date(self, branch='main'):
        self.commit_date = commits.get_commit_data(branch)
        # 统计并可视化 提交 频率
        commit_frequency = self.commit_date.resample('W').size() # 按周进行重采样

        plt.figure(figsize = (15, 10))
        commit_frequency.plot(kind = 'bar')
        plt.title(f'Commit Frequency over Time - {branch}')
        plt.xlabel('Date')
        plt.ylabel('Number of Commits')
        plt.tight_layout()
        plt.show()

    def visualize_commit_author(self, branch='main'):
        self.commit_author = commits.get_commit_data(branch)
        author_counts = self.commit_author['author'].value_counts()

        plt.figure(figsize=(15, 10))
        author_counts.plot(kind='bar')
        plt.title(f'Commit Counts by Author - {branch}')
        plt.xlabel('Author')
        plt.ylabel('Number of Commits')
        plt.tight_layout()
        plt.show()

    def visualize_commit_categories(self, branch='main'):
        self.commit_categories = commits.categorize_commits(commits.get_commit_data(branch))

        # 统计不同类别提交的数量
        category_counts = self.commit_categories['category'].value_counts()

        # 绘制饼图
        plt.figure(figsize=(8, 8))
        category_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.title(f'Commit Categories - {branch}')
        plt.ylabel('')  # Remove y-axis label
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":

    # 克隆仓库
    repo_manager = RepoManager(REPO_URL)
    repo_manager.clone_repo()

    visualizer = Visualizer()
    commits = Commits()

    visualizer.visualize_commit_date()
    visualizer.visualize_commit_categories('dev_1203')
    visualizer.visualize_commit_author('main')




