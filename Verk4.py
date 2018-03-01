from bottle import route, run, error, static_file, template
import os

import json
"""
f = open("bekkur.json", "r")
bekkur = json.load(f)
f.close()

bekkur["nemendur",][0]["kt"]
"""
with open("bekkur.json", "r", encoding="utf-8") as f:
    bekkur = json.load(f)

@route("/")
def index():
    return template("index", bekkur=bekkur)

@route("/nemandi/<kt>")
def nemandi(kt):
    return template("nemandi", kt=kt, bekkur=bekkur)

@route("/static/<filename>")
def server_static(filename):
    return static_file(filename, root="./myfiles")

@error(404)
def error404(error):
    return "Þessi síða er ekki til"

@error(500)
def error404(error):
    return "Þessi síða er ekki til"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
