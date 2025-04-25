# -*- coding: UTF-8 -*-
"""
    @Project : flaskdata 
    @File    : run.py
    @Author  : XianZS
    @meaning : 
"""
from flask import Flask, jsonify, request
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)
CORS(app)
Swagger(app)


@app.route('/api/user/<string:name>', methods=['GET'])
def get_user(name):
    """
    根据用户名和年龄查询用户信息
    ---
    tags:
      - 用户管理
    parameters:
      - name: name
        in: path
        type: string
        required: true
        description: 用户名
    responses:
      200:
        description: 成功返回用户信息
    """
    # 业务逻辑
    if name == "jom":
        return "hello jom"
    else:
        return "hello world"


if __name__ == '__main__':
    app.run(debug=True)
