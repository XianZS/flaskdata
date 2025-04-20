# -*- coding: UTF-8 -*-
"""
    @Project : flaskdata 
    @File    : __init__.py
    @Author  : XianZS
    @meaning : 
"""

from get_path import getPathMain as _getPathMain
from get_file_name import getFileNameMain as _getFileNameMain

getPathMain = _getPathMain
getFileNameMain = _getFileNameMain

if __name__ == '__main__':
    print(_getPathMain.get_file_path())
    print(_getFileNameMain.get_file_name())
    print(__file__)
