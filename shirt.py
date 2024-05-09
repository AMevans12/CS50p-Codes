import sys
from PIL import Image, ImageOps


def main():
    arguments()
    try:
        img = Image.open(sys.argv[1])
    except FileNotFoundError:
        print('Unable to open', sys.argv[1])
        sys.exit(1)  # Exit if the input file cannot be opened

    shirtfile = Image.open('shirt.png')
    size = shirtfile.size
    muppet = ImageOps.fit(img, size)
    muppet.paste(shirtfile, shirtfile)
    muppet.save(sys.argv[2])


def arguments():
    if len(sys.argv) != 3:
        print('Usage: python script.py input_image output_image')
        sys.exit(1)

    input_extension = sys.argv[1].split('.')[-1].lower()
    output_extension = sys.argv[2].split('.')[-1].lower()

    valid_extensions = ['png', 'jpeg', 'jpg']

    if input_extension not in valid_extensions or output_extension not in valid_extensions:
        print('Invalid Input: Both input and output images must be PNG, JPG, or JPEG files.')
        sys.exit(1)

    if input_extension != output_extension:
        print('Invalid Input: Input and output images must have the same extension.')
        sys.exit(1)


if __name__ == '__main__':
    main()
