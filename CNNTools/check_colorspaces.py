from scipy.misc import imread, imsave, imresize
import argparse
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help='input folder with images to process')
    args = parser.parse_args()

    if not os.path.isdir(args.input):
        exit('Input is not a folder')

    # Get all absolute paths for files in given directory
    images_paths = [os.path.abspath(os.path.join(dirpath, filename)) for dirpath, dirnames, filenames in os.walk(args.input) for filename in filenames if not filename.endswith('xml')]
    
    count = 0
    gray_names = []

    for file_path in images_paths:
        print(file_path, 'Colorspace:')
        image = imread(file_path)
        if len(image.shape) < 3:
            print('Gray')
            count += 1
            gray_names.append(file_path)
        elif len(image.shape) == 3:
            print('Color(RGB)')
        elif len(image.shape) == 4:
            print('Color(RGBA)')

    print(count)
    print(gray_names)