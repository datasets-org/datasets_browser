import argparse
import copy
import os
from datetime import datetime

import markdown
from flask import Flask
from flask import Markup
from flask import g
from flask import render_template

from confobj import ConfigEnv
from confobj import ConfigJson
from confobj import ConfigYaml
from datasets_lib import Datasets
from datasets_lib import DatasetsConfig
from web_config import WebConfig

app = Flask(__name__)


def get_ds(conf_order=None):
    ds = getattr(g, '_ds', None)
    if ds is None:
        if not conf_order:
            conf_order = (ConfigEnv(),)
        ds = g._ds = Datasets(DatasetsConfig(order=conf_order))
    return ds


def get_conf(conf_order=None):
    conf = getattr(g, '_conf', None)
    if conf is None:
        if not conf_order:
            conf_order = (ConfigEnv(),)
        conf = g._conf = WebConfig(order=conf_order)
    return conf


@app.route("/")
def main():
    ds = get_ds()
    try:
        data = ds.list()
    except Exception as e:
        return "Server error ({}) {}".format(ds.get_address(), e), 500
    # todo support server side sort
    data = sorted(data.items(), key=lambda x: x[1]["name"])
    return render_template('index.html', data=data)


@app.route('/detail/<ds_id>')
def detail(ds_id: str):
    ds = get_ds()
    conf = get_conf()
    try:
        data = ds.project_details(ds_id)
    except Exception as e:
        return "Server error ({}) {}".format(ds.get_address(), e), 500

    process_changelog(data, conf)
    process_usages(data, conf)
    markdowns = process_markdowns(data)

    processed = conf.processed
    return render_template('detail.html',
                           ds=data,
                           processed=processed,
                           id=ds_id,
                           markdowns=markdowns)


def process_changelog(data, conf):
    if not ("changelog" in data and data["changelog"]):
        return
    for i in data["changelog"]:
        for c in i:
            c[3] = format_date(c[3], conf.date_format)


def process_usages(data, conf):
    if not ("usages" in data and data["usages"]):
        return
    for c, i in enumerate(data["usages"]):
        d = copy.deepcopy(i)
        del d["timestamp"]
        data["usages"][c] = (format_date(i["timestamp"], conf.date_format), d)


def process_markdowns(data):
    markdowns = {}
    if not ("markdowns" in data and data["markdowns"]):
        return markdowns
    for m in data["markdowns"]:
        try:
            markdowns[m] = Markup(markdown.markdown(open(m).read()))
        except Exception as e:
            print(e)
    return markdowns


def format_date(val: str, date_format: str):
    return datetime.fromtimestamp(val).strftime(date_format)


def get_conf_type(path):
    if path == "ENV":
        return ConfigEnv()
    _, ext = os.path.splitext(i)
    if ext == ".json":
        return ConfigJson(path)
    if ext == ".yaml" or ext == ".yml":
        return ConfigYaml(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-dc', "--datasets-conf", nargs='*')
    parser.add_argument('-wc', "--web-conf", nargs='*')

    args = parser.parse_args()

    datasets_conf_order = []
    if args.datasets_conf is not None:
        for i in args.datasets_conf:
            datasets_conf_order.append(get_conf_type(i))

    server_conf_order = []
    if args.web_conf is not None:
        for i in args.web_conf:
            server_conf_order.append(get_conf_type(i))

    server_conf_order = tuple(server_conf_order) if server_conf_order else None
    datasets_conf_order = tuple(datasets_conf_order) if datasets_conf_order \
        else None
    with app.app_context():
        conf = get_conf(conf_order=server_conf_order)
        get_ds(conf_order=datasets_conf_order)
    app.run(host=conf.host,
            port=conf.port)
