import argparse
import os
import shutil
from xml.dom import minidom
import xml.etree.ElementTree as et
import glob

def count_labels_in_folder(files_paths):
    xmls_paths = sorted([x for x in files_paths if x.endswith('.xml')])

    labels_dict = {}

    for xml_path in xmls_paths:
        tree = et.parse(xml_path)
        root = tree.getroot()
        for child in root:
            if child.tag == 'object':
                for nested_child in child:
                    if nested_child.tag == 'name':
                        label_name = nested_child.text
                        if label_name in labels_dict:
                            labels_dict[label_name] += 1
                        else:
                            labels_dict[label_name] = 1
    
    return labels_dict


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help='input folder with images to process')

    args = parser.parse_args()

    input_folder = args.input

    if not os.path.isdir(input_folder):
        exit('Input is not a folder')

    train_folder_path = os.path.join(input_folder, 'train')
    test_folder_path = os.path.join(input_folder, 'test')

    files_paths = []
    train_files_paths = []
    test_files_paths = []
    
    # Get all absolute paths for files in given directory
    files_paths = [os.path.join(input_folder, file_name) for file_name in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, file_name))]

    try:
        train_files_paths = [os.path.join(train_folder_path, file_name) for file_name in os.listdir(train_folder_path) if os.path.isfile(os.path.join(train_folder_path, file_name))]
    except:
        print("Train folder not found")

    try:
        test_files_paths = [os.path.join(test_folder_path, file_name) for file_name in os.listdir(test_folder_path) if os.path.isfile(os.path.join(test_folder_path, file_name))]
    except:
        print("Test folder not found")


    all_labels_dict = count_labels_in_folder(files_paths)
    print('All files labels:')
    print(all_labels_dict)

    if train_files_paths and test_files_paths:
        train_labels_dict = count_labels_in_folder(train_files_paths)
        test_labels_dict = count_labels_in_folder(test_files_paths)

        print('Train files labels:')
        print(train_labels_dict)
        print('Test files labels')
        print(test_labels_dict)

        print('\n')
        for key in sorted(all_labels_dict):
            print('label:', key, '\t\ttrain ratio:', train_labels_dict[key] / float(all_labels_dict[key]), '\t\ttest ratio: ', test_labels_dict[key] / float(all_labels_dict[key]))                   
