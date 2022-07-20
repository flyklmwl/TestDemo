# 启动项目可以使用pycharm的Terminal客户端
# 注意要切换到对应的目录下面
# $env:FLASK_APP = "01 - hello world"
# flask run


from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True)
