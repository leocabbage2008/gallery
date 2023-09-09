from flask import Flask, render_template, send_from_directory
from glob import glob
import os, shutil

app = Flask(__name__)

try:
    dest = "./saves"
    for filename in glob("/Users/coder/saves/*.*"):
        shutil.copy(filename, dest)
finally:
    saves = "./saves"


@app.route("/")
def home():
    return "parked"


@app.route("/images/<filename>")
def serve_image(filename):
    path = os.path.join(saves, filename)
    if not os.path.exists(path):
        return "Image not found."
    return send_from_directory(saves, filename)


@app.route("/image_gallery")
def image_gallery():
    images = [
        (f, f.split(".")[1])
        for f in os.listdir(saves)
        if os.path.isfile(os.path.join(saves, f))
    ]
    return render_template("image_gallery.html", images=images)


@app.route("/read/<text>")
def nanny(text):
    return f"""lemme read you a bed time story kid
  once upon a time,
  {escape(text)}"""


@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)


if __name__ == "__main__":
    app.run(debug=True)
