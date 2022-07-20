from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def testvar():
    var1 = "变量1"
    dict1 = {
        "var2": {
            "link": "1",
            "变量3": "2",
        },
        "var3": {
            "变量4": "3",
            "link": "4",
        }
    }
    return render_template("index.html", var=var1, dict1=dict1)


if __name__ == '__main__':
    app.run(debug=True)
