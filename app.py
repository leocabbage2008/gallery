from flask import (
    Flask,
    render_template,
    send_from_directory,
    request,
    redirect,
    url_for,
)
from markupsafe import escape
from pathlib import Path
import random as r
import os, shutil

app = Flask(__name__)

# cache user options
# make right click copy optional
# make left click download optional
# figure out issue on azure where mp4's dont work well
# make some type of searching algo
# make a sorting algo


# try:
#     shutil.copytree("/Users/coder/saves", "./static/saves", dirs_exist_ok=True)
# except:
#     print("on virty pullin up with a hundre fitty")
saves = "./static/saves"
cats = "./static/cats"
images = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/gallery/<path:filename>")
def serve(filename):
    return send_from_directory(
        "static", os.path.join(request.args.get("path"), filename)
    )


@app.route("/random")
def random():
    images = [f for f in os.listdir(saves) if f.split(".")[-1] in "pnggifjpgjpegwebp"]
    i = r.choice(images)
    return send_from_directory("static", os.path.join("./saves", i))


@app.route("/randow")
def randow():
    videos = [f for f in os.listdir(saves) if f.split(".")[-1] in "webmmp4"]
    x = r.choice(videos)
    return send_from_directory("static", os.path.join("./saves", x))


@app.route("/gallery")
def gallery():
    password = request.args.get("password")
    if password == "pjoqfjopehnklewjjop56348890":
        images = [
            (str(f).split(r"/")[-1], str(f).split(r"/")[-1].split(".")[1], "./saves")
            for f in sorted(
                [x for x in Path(saves).iterdir() if not x.is_dir()],
                key=os.path.getmtime,
            )
        ]
    else:
        images = [
            (f, f.split(".")[1], "./cats")
            for f in os.listdir(cats)
            if os.path.isfile(os.path.join(cats, f))
        ]
    images = [x for x in images if x[1] in "pnggifjpgjpegwebp"]
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
