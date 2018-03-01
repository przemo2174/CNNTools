import cv2
from imgaug import augmenters as iaa
from scipy import misc
import os

class ImageModifier:
    def __init__(self, images_paths):
        sometimes = lambda aug: iaa.Sometimes(0.5, aug)
        self.seq = iaa.Sequential([       
            sometimes(iaa.Affine(
                scale={"x": (0.6, 1.5), "y": (0.6, 1.5)},
                rotate=(-45, 45)
            ))
            # iaa.GaussianBlur(sigma=(0, 3.0)) # blur images with a sigma of 0 to 3.0
            ])
        self.images_paths = images_paths
        self.modified_images = []        

    def modify_images(self, output_folder, images_number_to_generate):
        counter = 1
        images_data = [misc.imread(image_path) for image_path in self.images_paths]

        if not os.path.isdir(output_folder):
                os.makedirs(output_folder)

        for i in range(1, images_number_to_generate + 1):
            self.modified_images = self.seq.augment_images(images_data)
            
            for modify_image in self.modified_images:
                misc.imsave(os.path.join(output_folder, 'image_' + str(counter) + '.jpg'), modify_image)
                counter += 1