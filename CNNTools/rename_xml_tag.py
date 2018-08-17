import xml.etree.ElementTree as et
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help='input folder with images to process')
    parser.add_argument('--old', required=True)
    parser.add_argument('--new', required=True)

    args = parser.parse_args()

    input_folder = args.input
    old_tag = args.old
    new_tag = args.new

    if not os.path.isdir(input_folder):
        exit('Input is not a folder')

    # Get all absolute paths for files in given directory
    files_paths = [os.path.abspath(os.path.join(dirpath, filename)) for dirpath, dirnames, filenames in os.walk(input_folder) for filename in filenames]

    xmls_paths = sorted([x for x in files_paths if x.endswith('.xml')])


    for xml_path in xmls_paths:
        print('Modyfing', xml_path)
        tree = et.parse(xml_path)
        root = tree.getroot()
        for child in root:
            if child.tag == 'object':
                for nested_child in child:
                    if nested_child.tag == 'name':
                        if nested_child.text == old_tag:
                            nested_child.text = new_tag
        
        
        tree.write(xml_path)
    
    