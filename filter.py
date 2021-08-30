"""
This program implements a rad image filter.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'

def main():
    # Get file name from user input
    filename = get_file()
    
    # Load image and show image before the transform
    image = SimpleImage(filename)
    image.show()

    # Apply the filter
    filter_image = apply_filter(filename)
    

    # Show the image after the transform
    filter_image.show()

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename

def apply_filter(filename):
    image = SimpleImage(filename)
    for pixel in image:
        pixel.red = pixel.red*1.5
        pixel.green = pixel.green*0.7
        pixel.blue = pixel.blue*1.5
    return image



if __name__ == '__main__':
    main()
