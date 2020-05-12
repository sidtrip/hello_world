"""
File: codeinplace_filter.py
----------------
This program implements a rad image filter.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the image before the transform
    image.show()

    image = code_in_place_filter(filename)

    # Show the image after the transform
    image.show()

def code_in_place_filter(filename):
    processed = SimpleImage(filename)
    for px in processed:
        px.red = px.red * 1.5
        px.green = px.green * 0.7
        px.blue = px.blue * 1.5
    return processed

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()