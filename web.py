import copy
import os
from datetime import datetime

import markdown
import yaml
from flask import Flask
from flask import Markup
from flask import render_template

from ds.config import Config
from ds.datasets import Datasets

app = Flask(__name__)

# todo move config to method
address = None
try:
    cfg = yaml.load(open("conf/config.yaml"))
    address = cfg["server"]
except Exception as e:
    print(e)

if "server" in os.environ:
    address = os.environ["server"]

if not address:
    raise Exception("Server address is not specified")

# todo backend class


ds = Datasets(Config())


@app.route("/")
def main():
    data = ds.list_projects()
    data = sorted(data.items(), key=lambda x: x[1]["name"])
    return render_template('index.html', data=data)


@app.route('/detail/<ds_id>')
def detail(ds_id: str):
    data = ds.project_details(ds_id)
    # todo configurable processed
    processed = {'name', "usages", "maintainer", "paths", "tags", "links",
                 "markdowns", "_markdowns", "changelog", "_paths", "_links",
                 "internal", "data", "type", "url", "from", "characteristics"}
    markdowns = {}
    # changelog time format
    # todo configurable format
    if "changelog" in data and data["changelog"]:
        for i in data["changelog"]:
            for c in i:
                c[3] = datetime.fromtimestamp(c[3]).strftime("%d.%m.%Y %H:%M")

    if "usages" in data and data["usages"]:
        for c, i in enumerate(data["usages"]):
            d = copy.deepcopy(i)
            del d["timestamp"]
            data["usages"][c] = (
                datetime.fromtimestamp(i["timestamp"]).strftime(
                    "%d.%m.%Y %H:%M"), d)

    if "markdowns" in data and data["markdowns"]:
        for m in data["markdowns"]:
            try:
                markdowns[m] = Markup(markdown.markdown(open(m).read()))
            except Exception as e:
                print(e)
    return render_template('detail.html', ds=data, processed=processed,
                           id=ds_id,
                           markdowns=markdowns)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
