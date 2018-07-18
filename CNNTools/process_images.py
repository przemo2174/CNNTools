from scipy.misc import imread, imsave, imresize
from PIL import Image
import argparse
import os
import shutil
from pathlib import Path
import cv2


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help='input folder with images to process')
    parser.add_argument('-o', '--output', required=True, help='output folder to save images')
    args = parser.parse_args()

    if not os.path.isdir(args.input):
        exit('Input is not a folder')

    if os.path.isdir(args.output):
        shutil.rmtree(args.output)

    os.mkdir(args.output)

    # Get all absolute paths for files in given directory
    # images_paths = [os.path.abspath(os.path.join(dirpath, filename)) for dirpath, dirnames, filenames os.walk(args.input) for filename in filenames if not filename.endswith('xml')]
    images_paths = [os.path.abspath(os.path.join(args.input, filename)) for filename in os.scandir(args.input) if os.path.isfile(filename)]

    for image_path in images_paths:
        if image_path.endswith('.png'):           
           os.remove(image_path)
           print('Removed', image_path)
           corresponding_xml_path = image_path[:-3] + str('xml')

           if os.path.isfile(corresponding_xml_path):
               os.remove(corresponding_xml_path)
               print('Removed', corresponding_xml_path)

        elif image_path.endswith('.jpg'):
            print('Copying', image_path, 'to', os.path.join(args.output, os.path.basename(image_path)))
            shutil.copyfile(image_path, os.path.join(args.output, os.path.basename(image_path)))