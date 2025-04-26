# -*- coding: UTF-8 -*-
"""
    @Project : flaskdata 
    @File    : run.py
    @Author  : XianZS
    @meaning : 
"""
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__,
            template_folder="/flaskdata/app/templates", )
CORS(app)


# Swagger(app)


@app.route('/test1/<name>/<address>')
def test1(name, address):
    if name == "main_test":
        strs = "main_test_" + str(address) + ".html"
        print("strs:", strs)
        return render_template("main_test_1.html")
    else:
        return "error"


if __name__ == '__main__':
    app.run(debug=True)
