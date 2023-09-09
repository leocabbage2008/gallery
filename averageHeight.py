from PIL import Image
from glob import glob
import os
import ffmpeg

imgFileTypes=['gif','jpg','jpeg','webp']
imgFiles = sum([glob(f"./saves/*.{t}") for t in imgFileTypes],[])
vidFileTypes=['mov','mp4','webm']
vidFiles = sum([glob(f"./saves/*.{t}") for t in vidFileTypes],[])
averageHeight=0
for filepath in imgFiles:
  img = Image.open(filepath)
  averageHeight+=img.height
for filepath in vidFiles:
  probe=ffmpeg.probe(filepath)["streams"]
  try:
    averageHeight+=probe[0]["height"]
  except: 
    #mov
    averageHeight+=probe[1]["height"]


averageHeight/=len(imgFiles)+len(vidFiles)
print("average:",averageHeight)
