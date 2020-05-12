"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import random
N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    final_image = make(final_image)
    # This is an example which should generate a pinkish patch
    final_image.show()

def make(final_image):
    for i in range(N_ROWS):
        for j in range (N_COLS):

            a = random.choice([0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6])
            b = random.choice([0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6])
            c = random.choice([0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6])

            patch = make_recolored_patch(a, b, c)
            for px in patch:
                final_image.set_pixel(px.x + PATCH_SIZE * j, px.y + PATCH_SIZE * i, px)
    return final_image


def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    patch = SimpleImage(PATCH_NAME)
    # TODO: your code here.
    for px in patch:
        px.red = px.red * red_scale
        px.green = px.green * green_scale
        px. blue = px.blue * blue_scale

    return patch

if __name__ == '__main__':
    main()