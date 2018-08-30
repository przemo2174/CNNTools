import argparse
import os
import shutil
from xml.dom import minidom
import xml.etree.ElementTree as et
import glob
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np

class LabelsCounter:
    def count_labels(self, folder_path):
        if not os.path.isdir(folder_path):
            raise Exception("Input path is not a folder")

        xmls_paths = self.get_all_xml_files_paths(folder_path)

        labels_dict = {}
        xmls_labels_count = {}
        
        for xml_path in xmls_paths:
            label_count = 0
            tree = et.parse(xml_path)
            root = tree.getroot()
            for child in root:
                if child.tag == 'object':
                    for nested_child in child:
                        if nested_child.tag == 'name':
                            label_name = nested_child.text
                            label_count += 1
                            if label_name in labels_dict:
                                labels_dict[label_name] += 1
                            else:
                                labels_dict[label_name] = 1

            xmls_labels_count[xml_path] = label_count

        return labels_dict, xmls_labels_count

    def get_all_xml_files_paths(self, folder_path):

        if not os.path.isdir(folder_path):
            raise Exception("Input path is not a folder")

        # Get all absolute paths for files in given directory
        xmls_paths = [os.path.abspath(os.path.join(dirpath, filename)) for dirpath, dirnames, filenames in os.walk(folder_path) for filename in filenames if filename.endswith('xml')]
        return xmls_paths

    def show_labels_diagram(self, labels_dict, title='Music Notes Labels'):
        labels = list(labels_dict.keys())
        values = list(labels_dict.values())

        y_pos = np.arange(len(labels))

        plt.bar(y_pos, values, align='center')
        plt.xticks(y_pos, labels)
        plt.title(title)
 
        plt.show()

        

def count_labels_in_folder(files_paths):
    xmls_paths = sorted([x for x in files_paths if x.endswith('.xml')])

    labels_dict = {}
    xmls_labels_count = {}

    for xml_path in xmls_paths:
        label_count = 0
        tree = et.parse(xml_path)
        root = tree.getroot()
        for child in root:
            if child.tag == 'object':
                for nested_child in child:
                    if nested_child.tag == 'name':
                        label_name = nested_child.text
                        label_count += 1
                        if label_name in labels_dict:
                            labels_dict[label_name] += 1
                        else:
                            labels_dict[label_name] = 1

        xmls_labels_count[xml_path] = label_count

    return labels_dict, xmls_labels_count

def pretty_print(dictionary):
    for key, value in dictionary.items():
        print(key, "\t", value)



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


    all_labels_dict, xmls_labels = count_labels_in_folder(files_paths)
    print('All files labels:')
    pretty_print(all_labels_dict)
    pretty_print(xmls_labels)

    if train_files_paths and test_files_paths:
        train_labels_dict, _ = count_labels_in_folder(train_files_paths)
        test_labels_dict, _ = count_labels_in_folder(test_files_paths)

        print('Train files labels:')
        print(train_labels_dict)
        print('Test files labels')
        print(test_labels_dict)

        print('\n')
        for key in sorted(all_labels_dict):
            print('label:', key, '\t\ttrain ratio:', train_labels_dict[key] / float(all_labels_dict[key]), '\t\ttest ratio: ', test_labels_dict[key] / float(all_labels_dict[key]))                   
