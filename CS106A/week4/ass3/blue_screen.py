"""
File: bluescreen.py
----------------
Not part of the assignment. This was a lecture demo!
This is a fun algorithm to implement. It is not in the
assignment, but feel free to implement it as an extension.
Put the smaller foreground picture into the background.
Do not include any pixels that are sufficiently blue.
"""

from simpleimage import SimpleImage


def main():
    foreground = SimpleImage('images/tiefighter.jpg')
    background = SimpleImage('images/quad.jpg')
    for px in foreground:
        if blue_enough(px):
            foreground.set_pixel(px.x, px.y, background.get_pixel(px.x, px.y))
    background.show()
    foreground.show()

def blue_enough(px):
    if px.blue > 1.6 * ((px.red + px.green + px.blue) //3):
        return True
    else:
        False


if __name__ == '__main__':
    main()