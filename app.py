from flask import Flask, render_template, send_from_directory, request
from markupsafe import escape

import os, shutil

config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
}
app = Flask(__name__)

# try:
#     shutil.copytree("/Users/coder/saves", "./static/saves", dirs_exist_ok=True)
# except:
#     print("on virty pullin up with a hundre fitty")
saves = "./static/saves"
cats = "./static/cats"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/gallery/<path:filename>")
def serve(filename):
    return send_from_directory(
        "static", os.path.join(request.args.get("path"), filename)
    )


@app.route("/gallery")
# @cache.cached(timeout=300)
def gallery():
    password = request.args.get("password")
    print(password)
    if password == "pjoqfjopehnklewjjop56348890":
        images = [
            (f, f.split(".")[1], "./saves")
            for f in os.listdir(saves)
            if os.path.isfile(os.path.join(saves, f))
        ]
    else:
        images = [
            (f, f.split(".")[1], "./cats")
            for f in os.listdir(cats)
            if os.path.isfile(os.path.join(cats, f))
        ]
    return render_template("gallery.html", images=images)


@app.route("/read/<text>")
def nanny(text):
    return f"""lemme read you a bed time story kid
  once upon a time,
  {escape(text)}"""


@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)


if __name__ == "__main__":
    app.run()
