from flask import Flask
from Utils import SCORES_FILE_NAME

app = Flask("Score server")


@app.route('/')
def score_server():
    try:
        score_file = open(SCORES_FILE_NAME, "r")
        score = score_file.read()
        score_file.close()
        site = f"<html><head><title>Scores Game</title><head><body><h1>The score is <div id=\"score\">{score}</div></h1></body></html>"
        return site
    except BaseException as e:
        print(e.args)
        error_site = f"<html><head><title>Scores Game</title><head><body><h1>The score is <div id=\"score\" style=\"color:red\">{e.args}</div></h1></body></html>"
        return error_site


app.run(host="0.0.0.0", port=5001, debug=True)
