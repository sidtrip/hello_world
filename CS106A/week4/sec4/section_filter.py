from simpleimage import SimpleImage
#narok
BRIGHT_THRESHOLD = 153 #(0.6*255)

def main():
    """
    This program loads an image and applies the narok filter
    to it by setting "bright" pixels to grayscale values.
    """
    image = SimpleImage('images/simba-sq.jpg')
        #for loop
        #pixel average --> get_pixel_average()
        #bright or not
    for pixel in image:
        pixel_avg = get_pixe_average(pixel)
        if pixel_avg > BRIGHT_THRESHOLD:
            pixel.red = pixel_avg
            pixel.blue = pixel_avg
            pixel.green = pixel_avg
        #if bright ---> pixel_avg > 153
        #apply grey scale ---> set rgb channel to px avg
    image.show()

    
def get_pixe_average(pixel):
    """
    input px    avg = avg of rgb      r+g+b//3
    """
    return (pixel.red+ pixel.green + pixel.blue )//3
    
    
if __name__ == '__main__':
    main()