# -*- coding: UTF-8 -*-
"""
    @Project : flaskdata 
    @File    : get_path.py
    @Author  : XianZS
    @meaning : 
"""
import os
import typing


class GetPath:
    __path = ""

    def __init__(self):
        self.__path = os.path.abspath('.')

    def get_path(self):
        return self.__path


class GetPathMain(GetPath):
    def get_file_path(self):
        return self.get_path()


getPathMain = GetPathMain()

if __name__ == '__main__':
    getPathMain = GetPathMain()
    print(getPathMain.get_file_path())
