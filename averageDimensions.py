from PIL import Image
from glob import glob
import os
import ffmpeg

imgFileTypes = ["gif", "jpg", "jpeg", "webp"]
imgFiles = sum([glob(f"./saves/*.{t}") for t in imgFileTypes], [])
vidFileTypes = ["mov", "mp4", "webm"]
vidFiles = sum([glob(f"./saves/*.{t}") for t in vidFileTypes], [])
averageHeight = 0
averageWidth = 0
for filepath in imgFiles:
    img = Image.open(filepath)
    averageHeight += img.height
    averageWidth += img.width
for filepath in vidFiles:
    probe = ffmpeg.probe(filepath)["streams"]
    try:
        averageHeight += probe[0]["height"]
        averageWidth += probe[0]["width"]
    except:
        # mov
        averageHeight += probe[1]["height"]
        averageWidth += probe[1]["width"]


averageHeight /= len(imgFiles) + len(vidFiles)
averageWidth /= len(imgFiles) + len(vidFiles)
print("average height:", averageHeight)
print("average width:", averageWidth)
