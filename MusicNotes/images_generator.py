import argparse
import sys
import os
from image_modifier import ImageModifier

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help='input folder with images to process')
    parser.add_argument('-o', '--output', required=True, help='output folder to save images')

    args = parser.parse_args()

    if os.path.isdir(args.input):
        images_paths = []
        for dirpath, dirnames, filenames in os.walk(args.input):
            for filename in filenames:
                images_paths.append(os.path.abspath(os.path.join(dirpath, filename)))    

        image_modifier = ImageModifier(images_paths)
        image_modifier.modify_images()        
    else:
        print(args.input, ' - folder not found', file=sys.stderr)
        sys.exit()

    


    



    

        