# coding=utf-8

# 重命名文件

import os

dir = "/Users/ooooo/Library/Favorites/Learning/03.Unity3D用户手册 53课"
os.chdir(dir)

for file in os.listdir(dir):
    if file.find("[www.17zixueba.com]")>=0:
        os.rename(file,file.replace("[www.17zixueba.com]",""))
    # print(file)
