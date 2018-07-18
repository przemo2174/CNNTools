import xml.etree.ElementTree as et
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help='input folder with images to process')

    args = parser.parse_args()

    input_folder = args.input

    item_to_remove = 'pipe'

    if not os.path.isdir(input_folder):
        exit('Input is not a folder')

    # Get all absolute paths for files in given directory
    files_paths = [os.path.abspath(os.path.join(dirpath, filename)) for dirpath, dirnames, filenames in os.walk(input_folder) for filename in filenames]

    xmls_paths = sorted([x for x in files_paths if x.endswith('.xml')])


    for xml_path in xmls_paths:
        print('Modyfing', xml_path)
        elements_to_remove = []
        tree = et.parse(xml_path)
        root = tree.getroot()
        for child in root:
            if child.tag == 'object':
                for nested_child in child:
                    if nested_child.tag == 'name':
                        if nested_child.text == item_to_remove:
                            elements_to_remove.append(child)
        
        for element in elements_to_remove:
            print('Removing', element)
            root.remove(element)
        
        tree.write(xml_path)
    
    