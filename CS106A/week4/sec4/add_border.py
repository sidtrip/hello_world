from simpleimage import SimpleImage

def main():
    image = SimpleImage('images/simba-sq.jpg')
    bordered_img = add_border(image, 10)
    bordered_img.show()


def add_border(original_img, border_size):
    """
    This function returns a new SimpleImage which is the same as
    original image except with a black border added around it. The
    border should be border_size many pixels thick.

    Inputs:
        - original_img: The original image to process
        - border_size: The thickness of the border to add around the image

    Returns:
        A new SimpleImage with the border added around original image
    """
    #if the pixel is in the border
    # add_border(img, size)
         #create new image 
    new_width = original_img.width + 2 * border_size
    new_height = original_img.height + 2 * border_size
    
    bordered_img = SimpleImage.blank(new_width, new_height)
    for x in range(bordered_img.width):
        for y in range(bordered_img.height):
            if is_border_pixel(x,y, border_size, bordered_img):
                pixel = bordered_img.get_pixel(x,y)
                pixel.red = 0
                pixel.green = 0
                pixel.blue = 0
                #add border
            else:
                orig_x = x - border_size
                orig_y = y - border_size
                orig_pixel = original_img.get_pixel(orig_x, orig_y)
                bordered_img.set_pixel(x, y, orig_pixel)
                #original image
                
                
                
    return bordered_img
def is_border_pixel(x,y, border_size, bordered_img):
    #left
    if x < border_size:
        return True
    #right
    if x >= bordered_img.width - border_size:
        return True
    #top
    if y < border_size:
        return True
    #bottom
    if y >= bordered_img.height - border_size:
        return True
    
    return False
                  
if __name__ == '__main__':
    main()