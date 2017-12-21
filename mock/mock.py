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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
