from simpleimage import SimpleImage

def main():
    image = SimpleImage('images/karel.png')
    trimmed_img = trim_crop_image(image, 30)
    trimmed_img.show()


def trim_crop_image(original_img, trim_size):
    """
    This function returns a new SimpleImage which is a trimmed and
    cropped version of the original image by shaving trim_sz pixels
    from each side (top, left, bottom, right) of the image. You may
    assume trim_sz is less than half the width of the image.

    Inputs:
        - original_img: The original image to process
        - trim_size: The number of pixels to shave from each side
                   of the original image

    Returns:
        A new SimpleImage with trim_sz pixels shaved off each
        side of the original image
    """
    nudimx = original_img.width - 2*trim_size 
    nudimy = original_img.height - 2*trim_size
    new = SimpleImage.blank(nudimx, nudimy)
    for y in range(new.height):
        for x in range(new.width):
            newx = x + trim_size-1
            newy = y + trim_size-1
            new.set_pixel(x, y, original_img.get_pixel(newx, newy))
    return new

if __name__ == '__main__':
    main()