import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=False, default='./', help='input folder with images to process')
    parser.add_argument('-n', '--name', required=False, default='image', help='base name for all images')   

    args = parser.parse_args()

    if not os.path.isdir(args.input):
        exit('Input is not a folder')
