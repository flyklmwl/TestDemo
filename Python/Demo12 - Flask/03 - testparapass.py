from flask import Flask
from flask import render_template


# 前后台的数据传输
# __name__ 就是该文件的文件名


app = Flask(__name__)


@app.route("/")
def testvar():
    return render_template("index.html")


@app.route("/hello")
def hello():
    return "hello, world"


if __name__ == '__main__':
    app.run(debug=True)
