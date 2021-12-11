import os
from PIL import Image

def conversion():
    colors = ['red', 'blue', 'yellow', 'green']
    # create a set of 4 files with the extension *.jpg
    for color in colors:
        img = Image.new('RGB', (60, 30), color=color)
        img.save(color + '_image.jpg')

    cwd = os.getcwd()
    for color in colors:
        path = os.path.join(cwd, color + "_image.jpg")
        new_extension_path = os.path.join(cwd, color + "_image.png")
        im1 = Image.open(path)
        im1.save(new_extension_path)

conversion()