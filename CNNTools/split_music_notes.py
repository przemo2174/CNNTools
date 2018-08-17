import argparse
import os
from numpy import random
from pathlib import Path
import shutil

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help='input folder with images to process')

    args = parser.parse_args()

    input_folder = args.input

    if not os.path.isdir(args.input):
        exit('Input is not a folder')

    music_notes_all = os.path.join(input_folder, "music_notes_all")
    if os.path.isdir(music_notes_all):
        shutil.rmtree(music_notes_all)

    
    notes_folders = [os.path.join(input_folder, directory) for directory in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, directory))]
    
    for note_folder in notes_folders:
        print(note_folder)
        os.system("python test_train_split.py -i " + note_folder +  ' --test=0.25 --train=0.75')

    
    

    music_notes_all_test_folder = os.path.join(music_notes_all, 'test')
    music_notes_all_train_folder = os.path.join(music_notes_all, 'train')

    os.mkdir(music_notes_all)
    os.mkdir(music_notes_all_test_folder)
    os.mkdir(music_notes_all_train_folder)

    for note_folder in notes_folders:
        test_folder = os.path.join(note_folder, 'test')
        train_folder = os.path.join(note_folder, 'train')

        test_files_paths = [os.path.join(test_folder, filename) for filename in os.listdir(test_folder)]
        train_files_paths = [os.path.join(train_folder, filename) for filename in os.listdir(train_folder)]

        for file_path in test_files_paths:
            print('Copying', file_path, 'to', os.path.join(music_notes_all_test_folder, Path(file_path).name))
            shutil.copyfile(file_path, os.path.join(music_notes_all_test_folder, Path(file_path).name))

        for file_path in train_files_paths:
            print('Copying', file_path, 'to', os.path.join(music_notes_all_train_folder, Path(file_path).name))
            shutil.copyfile(file_path, os.path.join(music_notes_all_train_folder, Path(file_path).name))




