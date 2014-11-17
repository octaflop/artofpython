# encoding: utf-8

from PIL import Image

def save_a_png(turtle, filename):
    ts = turtle.getscreen().getcanvas()
    epsfile = "{0}.eps".format(filename)
    ts.postscript(file=epsfile)
    pngfile = "{0}.png".format(filename)
    img = Image.open(epsfile)
    img.save(pngfile)
    return