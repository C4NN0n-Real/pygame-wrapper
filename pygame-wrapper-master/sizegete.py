from PIL import Image

def sizeget(img):
    im = Image.open(img)
    return im.size
