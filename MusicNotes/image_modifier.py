import cv2
from imgaug import augmenters as iaa
from scipy import misc
import os

class ImageModifier:
    def __init__(self, images_paths):
        sometimes = lambda aug: iaa.Sometimes(0.5, aug)
        self.seq = iaa.Sequential([       
            sometimes(iaa.Affine(
                scale={"x": (0.8, 1.2), "y": (0.8, 1.2)},
                rotate=(-45, 45)
            ))
            # iaa.GaussianBlur(sigma=(0, 3.0)) # blur images with a sigma of 0 to 3.0
            ])
        self.images_paths = images_paths
        self.modified_images = []        

    def modify_images(self):
        images_data = [misc.imread(image_path) for image_path in self.images_paths]
        self.modified_images = self.seq.augment_images(images_data)
        i = 1
        if not os.path.isdir('modified'):
            os.makedirs('modified')
        for modify_image in self.modified_images:
            misc.imsave(os.path.join('modified', 'image_' + str(i) + '.jpg'), modify_image)
            i += 1


        
