# -- coding: utf-8 --**

from flask import Flask, request
from flask import render_template


## 接收ajax 传输过来的json

app = Flask(__name__)


@app.route("/")
def testvar():
    return render_template("TestAjax.html")


@app.route("/recivied", methods=['post'])
def reci():
    data = request.json
    print(data)
    return "success"


if __name__ == '__main__':
    app.run(debug=True)
