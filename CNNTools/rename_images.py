import argparse
import os
import shutil
from xml.dom import minidom
import xml.etree.ElementTree as et

# The script changes name for all images based on base name, it also finds xml file corresponding to this image if exsits, change it's name and looks inside 
# in xml tag and also change it's name there.

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help='input folder with images to process')
    parser.add_argument('-n', '--name', required=False, default='image', help='base name for all images')
    parser.add_argument('-o', '--output', required=True, help='output folder to save processed files')
    parser.add_argument('--start', required=False, default=1)   

    args = parser.parse_args()

    input_folder = args.input
    output_folder = args.output
    base_name = args.name

    if not os.path.isdir(input_folder):
        exit('Input is not a folder')

    if os.path.isdir(output_folder):
        shutil.rmtree(output_folder)

    os.mkdir(output_folder)

    # Get all absolute paths for files in given directory
    files_paths = [os.path.abspath(os.path.join(dirpath, filename)) for dirpath, dirnames, filenames in os.walk(input_folder) for filename in filenames]

    images_paths = sorted([x for x in files_paths if not x.endswith('.xml')])
    xmls_paths = sorted([x for x in files_paths if x.endswith('.xml')])

    counter = int(args.start)

    for image_path in images_paths:
        image_name_without_extension, image_extension = os.path.splitext(os.path.basename(image_path))
        xml_path = None

        try:
            xml_path_index = xmls_paths.index(os.path.join(input_folder, image_name_without_extension) + '.xml')
            xml_path = xmls_paths[xml_path_index]
        except ValueError:
            xml_path = None
        
        #Copy file to output folder
        new_image_name = base_name + '_' + str(counter) + image_extension
        new_image_path = os.path.join(output_folder, new_image_name)
        shutil.copyfile(image_path, new_image_path)
        print('Copying', image_path, 'to', new_image_path)

        if xml_path is not None:
            new_xml_name = base_name + '_' + str(counter) + '.xml'
            new_xml_path = os.path.join(output_folder, new_xml_name)
            shutil.copyfile(xml_path, new_xml_path)
            print('Copying', xml_path, 'to', new_xml_path)

            #change reference image in xml tag
            tree = et.parse(new_xml_path)
            root = tree.getroot()
            for child in root:
                if child.tag == 'filename':
                    child.text = new_image_name
            tree.write(new_xml_path)
           
        counter += 1
        
        


