# coding=utf-8

# 重命名文件

import os

dir = "/Users/ooooo/Library/Favorites/Learning/03.Unity3D用户手册 53课"
os.chdir(dir)

for file_path in os.listdir(dir):
    if file_path.find("[www.17zixueba.com]") >= 0:
        os.rename(file_path, file_path.replace("[www.17zixueba.com]", ""))
    # print(file)
