import pyscreeze

def pixel(x,y):
    im = pyscreeze.screenshot(region=(x,y, x+1, y+1))
    px = im.getpixel((x,y))

    return px

