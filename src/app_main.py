# -*- coding: UTF-8 -*-
"""
    @Project : flaskdata 
    @File    : app_main.py
    @Author  : XianZS
    @meaning : 
"""
import os
import sys
from flask import Flask, request, jsonify


class RunMethod:
    """
        run method
        (1) run method at debug
        (2) run method at localhost
    """
    pass

class AppMain:
    def __init__(self):
        self.app = Flask(__name__)


if __name__ == "__main__":
    print(__name__)
