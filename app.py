from flask import Flask, render_template, request, redirect
import random
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

app = Flask(__name__)

s3 = boto3.client("s3")
bucket = "cranky"
saves = "saves/"
cats = "cats/"


def listFiles(bucket, prefix):
    response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
    files = [obj["Key"] for obj in response.get("Contents", []) if obj["Key"] != prefix]
    return files


def url(filename, f):
    return f"https://{bucket}.s3.us-east-2.amazonaws.com/{f}{filename}"


saveFiles = listFiles(bucket, saves)
catFiles = listFiles(bucket, cats)
allFiles = saveFiles + catFiles


def filter(ext):
    return [f for f in allFiles if f.split(".")[-1].lower() in ext]


def getPrefix(image):
    if image in listFiles(bucket, saves):
        return saves
    return cats


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/gallery")
def gallery():
    password = request.args.get("password") == "pjoqfjopehnklewjjop56348890"
    images = [
        (
            f.split("/")[-1],
            f.split(".")[-1],
            url(f.split("/")[-1], saves if password else cats),
        )
        for f in sorted(saveFiles if password else catFiles)
    ]
    images = [
        x for x in images if x[1].lower() in ["png", "gif", "jpg", "jpeg", "webp"]
    ]
    return render_template("gallery.html", images=images)


@app.route("/serve/<path:filename>")
def serve(filename):
    return redirect(url(filename, getPrefix(filename)))


@app.route("/random")
def random_image():
    images = filter(["png", "gif", "jpg", "jpeg", "webp"])
    r = random.choice(images)
    return redirect(url(r), getPrefix(r))


@app.route("/randow")
def random_video():
    videos = filter(["webm", "mp4"])
    r = random.choice(videos)
    redirect(url(r), getPrefix(r))


if __name__ == "__main__":
    app.run()
