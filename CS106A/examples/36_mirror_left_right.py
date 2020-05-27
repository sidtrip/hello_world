from simpleimage import SimpleImage

def main():
    original = SimpleImage('Screenshot 2020-05-25 at 10.01.52 PM.png')
    original.show()

    mirrored = mirror(original)
    mirrored.show()
def mirror(original):
    mirrored = SimpleImage.blank(original.width*2, original.height)
    for y in range(original.height):
        for x in range(original.width):
            pixel = original.get_pixel(x, y)
            mirrored.set_pixel(x, y, pixel)
            mirrored.set_pixel((original.width * 2) - (x + 1), y, pixel)
    return mirrored



if __name__ == "__main__":
    main()