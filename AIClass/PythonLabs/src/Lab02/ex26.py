import os
import imghdr
from PIL import Image
import sys

fileName = sys.argv[1]

if os.path.exists(fileName) and imghdr.what(fileName):
    with Image.open(fileName) as img:
        width, height = img.size
        print("The size of the image is width=", width, " height=", height)
else:
    print("The given file isn't an image file")