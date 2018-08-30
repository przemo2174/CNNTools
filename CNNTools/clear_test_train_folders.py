import argparse
import os
import shutil

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help='input folder with images to process')

    args = parser.parse_args()

    input_folder = args.input

    if not os.path.isdir(input_folder):
        exit('Input is not a folder')

    for dirpath, dirnames, filenames in os.walk(input_folder):
        if dirpath.endswith('test') or dirpath.endswith('train'):
            print('Removing', dirpath)
            shutil.rmtree(dirpath)