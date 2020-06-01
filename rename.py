import os
from os import listdir
from PIL import Image

dir_path = os.path.dirname(os.path.realpath(__file__))
image_path = dir_path + "/Images/landing/"

# find images
images = [f for f in listdir(image_path) if f[-4:] != ".txt"]
images_new = [i for i in images if len(i) != 7]

# get current number of images
current_n = len(images) - len(images_new)

print(f"Current number of Images: {current_n}\n")

size = 400, 400

# resize and rename images
for image in images_new:
    current_n += 1
    infile = image_path + image
    if len(str(current_n)) == 1:
        outfile = image_path + "00" + str(current_n) + ".jpg"
    elif len(str(current_n)) == 2:
        outfile = image_path + "0" + str(current_n) + ".jpg"
    else:
        print("Image limit exceeded")
        break
    im = Image.open(infile)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(outfile, "jpeg")
    os.remove(infile)

print(f"Resizing and renaming complete.\n\nSee {image_path}")

