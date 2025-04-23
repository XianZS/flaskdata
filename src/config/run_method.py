# -*- coding: UTF-8 -*-
"""
    @Project : flaskdata 
    @File    : run_method.py
    @Author  : XianZS
    @meaning : 运行方式，debug模式，本地模式
"""

import os
import sys
from abc import ABC, abstractmethod


class RunMethod(ABC):
    @abstractmethod
    def run_localhost(self, app_main):
        """ 运行本地模式 """
        """ localhost run """
        pass

    @abstractmethod
    def run_debug(self, app_main):
        """ 运行debug模式 """
        """ debug run """
        pass


class RunMethodMain(RunMethod):
    __app_main = None

    def run_localhost(self, app_main):
        """ 运行本地模式 """
        """ localhost run """
        self.__app_main = app_main
        self.__app_main.run()

    def run_debug(self, app_main):
        """ 运行debug模式 """
        """ debug run """
        self.__app_main = app_main
        # 配置host
        host = '0.0.0.0'
        # 配置端口
        port = 8080
        # 配置debug
        debug = True
        self.__app_main.run(port=port, debug=debug, host=host)


if __name__ == '__main__':
    pass
