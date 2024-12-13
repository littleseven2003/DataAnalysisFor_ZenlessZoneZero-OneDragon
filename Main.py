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
    def visualize_commit_frequency(self, branch, commit_data):
        # 统计并可视化 提交 频率
        commit_frequency = commit_data.resample('W').size() # 按周进行重采样

        plt.figure(figsize = (15, 10))
        commit_frequency.plot(kind = 'bar')
        plt.title(f'Commit Frequency over Time - {branch}')
        plt.xlabel('Date')
        plt.ylabel('Number of Commits')
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":

    # 克隆仓库
    repo_manager = RepoManager(REPO_URL)
    repo_manager.clone_repo()

    visualizer = Visualizer()

    commits = Commits()
    commit_data_all = commits.get_commit_data_all('dev_1203')
    commit_data_main = commits.get_commit_data_main()
    visualizer.visualize_commit_frequency('dev_1203', commit_data_all)
    visualizer.visualize_commit_frequency('main', commit_data_main)



