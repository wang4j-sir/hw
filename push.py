# -*- coding: utf8 -*-
# ！/usr/bin/env python

import os
import shutil
import sys

# git clone的目录
gitDir = "C:\\Users\\1\\Desktop\\hw\\"
# 文件分片的目录
fileDir = "C:\\Users\\1\\Desktop\\gulivideo\\"

def push():
    """
    获取目录所有分片文件
    """
    list = os.listdir(fileDir)
    for name in list:
        if ".rar" in name:
            from_file_path = fileDir + name
            target_file_path = gitDir + name
            shutil.move(from_file_path,target_file_path)
            os.system("git add . && git commit -m 1 && git push")
    exit()        


if __name__=='__main__':
   push()