import copy
import markdown
import os
import requests
import yaml
from datetime import datetime
from flask import Flask
from flask import Markup
from flask import render_template

app = Flask(__name__)
cfg = yaml.load(open("conf/config.yaml"))

address = cfg["server"]


@app.route("/")
def main():
    data = requests.get(address).json()
    data = sorted(data.items(), key=lambda x: x[1]["name"])
    return render_template('index.html', data=data)


@app.route('/detail/<id>')
def detail(id):
    data = requests.get(address + "detail/" + id).json()
    processed = {'name', "usages", "maintainer", "paths", "tags", "links",
                 "markdowns", "_markdowns", "changelog", "_paths", "_links",
                 "internal", "data", "type", "url", "from", "characteristics"}
    markdowns = {}
    # changelog time format
    if "changelog" in data:
        for i in data["changelog"]:
            for c in i:
                c[3] = datetime.fromtimestamp(c[3]).strftime("%d.%m.%Y %H:%M")

    if "usages" in data:
        for c, i in enumerate(data["usages"]):
            d = copy.deepcopy(i)
            del d["timestamp"]
            data["usages"][c] = (
                datetime.fromtimestamp(i["timestamp"]).strftime(
                    "%d.%m.%Y %H:%M"), d)

    if "markdowns" in data:
        for m in data["markdowns"]:
            try:
                markdowns[m] = Markup(markdown.markdown(open(m).read()))
            except Exception as e:
                print(e)
    return render_template('detail.html', ds=data, processed=processed, id=id,
                           markdowns=markdowns)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
