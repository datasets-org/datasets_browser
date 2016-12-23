from flask import Flask

app = Flask(__name__)

# from conf import Cfg

import os
from flask import render_template
import requests

# cfg = Cfg()

address = "http://192.168.1.143:8000/"


@app.route("/")
def main():
    data = requests.get(address).json()
    data = sorted(data.items(), key=lambda x: x[1]["name"])
    return render_template('index.html', data=data)


@app.route('/detail/<id>')
def detail(id):
    data = requests.get(address + "detail/" + id).json()
    processed = {'name', "usages", "maintainer", "paths", "tags", "links"}
    return render_template('detail.html', ds=data, processed=processed, id=id)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
