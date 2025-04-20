# -*- coding: UTF-8 -*-
"""
    @Project : flaskdata 
    @File    : get_file_name.py
    @Author  : XianZS
    @meaning : 
"""
import os
import sys


class GetFileName:
    __file_name = ""

    def __init__(self):
        self.__file_name = os.path.basename(__file__)

    def file_name(self):
        return self.__file_name


class GetFileNameMain(GetFileName):
    def get_file_name(self):
        return self.file_name()


getFileNameMain = GetFileNameMain()

if __name__ == '__main__':
    getFileNameMain = GetFileNameMain()
    print(getFileNameMain.get_file_name())
