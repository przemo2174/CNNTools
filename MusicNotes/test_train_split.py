import argparse
import sys
import os
from numpy import random
from shutil import copyfile
from pathlib import Path
import shutil


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help='input folder with images to process')
    parser.add_argument('--test', required=False, default=0.3, type=float, help='proportion in 0.XX format how many percentage of images should be moved to test folder (default is 0.3)')
    parser.add_argument('--train', required=False, default=0.7, type=float, help='proportion in 0.XX format how many percentage of images should be moved to train folder (default is 0.7')

    args = parser.parse_args()
    
    print('Generating %0.1f%% train images and %0.1f%% test images...' % (args.train * 100, args.test * 100))

    if not os.path.isdir(args.input):
        exit('Input is not a folder')

    test_dataset_dir_path = os.path.join(args.input, 'test')
    train_dataset_dir_path = os.path.join(args.input, 'train')

    # Cleanup of previous test dataset
    if os.path.isdir(test_dataset_dir_path):
        shutil.rmtree(test_dataset_dir_path)

    # Cleanup of previous train dataset
    if os.path.isdir(train_dataset_dir_path):
        shutil.rmtree(train_dataset_dir_path)

    print('Test dataset will be placed here:', test_dataset_dir_path)
    print('Train dataset will be placed here:', train_dataset_dir_path)
    
    # Get all absolute paths for files in given directory
    files_paths = [os.path.abspath(os.path.join(dirpath, filename)) for dirpath, dirnames, filenames in os.walk(args.input) for filename in filenames]

    # Check if all images have xmls
    images_paths = sorted([x for x in files_paths if not x.endswith('.xml')])
    xmls_paths = sorted([x for x in files_paths if x.endswith('.xml')])

    images_paths_length = len(images_paths)
    xmls_paths_length = len(xmls_paths)

    if images_paths_length != xmls_paths_length:
        exit("Some images were untagged")
    
    images_xmls_dict = (dict(zip(images_paths, xmls_paths)))

    # take random images paths to test taking into account proportion
    test_images_paths = random.choice(images_paths, int(args.test * images_paths_length), replace=False)

    os.mkdir(test_dataset_dir_path)

    # copy randomly choosen images and xml to test dataset folder
    for image_path in test_images_paths:
        xml_path = images_xmls_dict[image_path]
        copyfile(image_path, os.path.join(test_dataset_dir_path, Path(image_path).name))
        copyfile(xml_path, os.path.join(test_dataset_dir_path, Path(xml_path).name))

    os.mkdir(train_dataset_dir_path)

    # get paths to images that were not inluded in test dataset
    train_images_paths = list(set(images_paths) - set(test_images_paths))

    # copy randomly choosen images and xml to train dataset folder
    for image_path in train_images_paths:
        xml_path = images_xmls_dict[image_path]
        copyfile(image_path, os.path.join(train_dataset_dir_path, Path(image_path).name))
        copyfile(xml_path, os.path.join(train_dataset_dir_path, Path(xml_path).name))

    print('Done...')
    print('All images count:', images_paths_length)
    print('Test images count:', len(test_images_paths))
    print('Train images count:', len(train_images_paths))


    






    





