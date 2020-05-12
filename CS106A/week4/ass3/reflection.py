"""
File: reflection.py
----------------
Take an image. Generate a new image with twice the height. The top half
of the image is the same as the original. The bottom half is the mirror
reflection of the top half.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage


def make_reflected(filename):
    image = SimpleImage(filename)

    new_blank = SimpleImage.blank(image.width, image.height*2)
    for y in range(image.height):
        for x in range(image.width):
            px = image.get_pixel(x, y)
            new_blank.set_pixel(x, y, px)
            y_coordinate_mirror = (2 * (image.height-1)) - y
            new_blank.set_pixel(x, y_coordinate_mirror, px)
    return new_blank


def main():
    """
    This program tests your highlight_fires function by displaying
    the original image of a fire as well as the resulting image
    from your highlight_fires function.
    """
    original = SimpleImage('images/mt-rainier.jpg')
    original.show()
    reflected = make_reflected('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
