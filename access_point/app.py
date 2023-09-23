from flask import request
import flask
import json

app = flask.Flask(__name__)




@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data_s = request.form
        print(data_s)
        key = data_s["api_key"]
        summ_id = data_s["summ_id"]
        diction =  {"api_key":key, "riot_id":summ_id}
        with open("../pass_through.json", "w") as f:
            json.dump(diction, f)
    return flask.render_template("index.html")

@app.route("/api/v1/api_key", methods=["GET"])
def key():
    key = ""
    summ_id = ""
    with open("../pass_through.json","r") as f:
        dump = json.load(f)
        key = dump["api_key"]
        summ_id = dump["riot_id"]

    return {"api_key": key, "summoner_id": summ_id}




if __name__ == "__main__":
    app.run()