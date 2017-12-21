import json

from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return json.dumps(
        {
            "5a8a97bd-2cbb-4069-afe2-7101450c99b4": {
                "tags": ["eml", "spam"],
                "paths": ["path/file"],
                "name": "Kaggle - spam mail ADCG_SS14"},
            "2f063b0b-5322-4bd9-aeff-4b1063479610": {
                "tags": ["txt"],
                "paths": ["w2w"],
                "name": "Google W2V"
            }
        }
    )


@app.route("/detail/<id>")
def detail(id):
    return json.dumps(
        {
            "id": "5a8a97bd-2cbb-4069-afe2-7101450c99b4",
            "tags": ["eml", "spam"],
            "paths": ["path/ds"],
            "links": ["pth/aaa"],
            "markdowns": ["pth/readme.md"],
            "data": ["data"],
            "url": "https://inclass.kaggle.com/c/adcg-ss14-challenge-02-spam"
                   "-mails-detection/data",
            "maintainer": "tivvit@example.com",
            "name": "Kaggle - spam mail ADCG_SS14",
            "characteristics": [
                ["data", [["extensions", {"eml": 4327, "ico": 500}],
                          ["files_cnt", 4334],
                          ["files_size", "34M"]]]
            ],
            "type": "fs",
            "changelog": [
                [["markdowns", [], ["pth/readme.md"], 1483053904.5619552135]],
                [["markdowns", [], ["path/readme.md"], 1483051504.5655066967]]
            ]
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
