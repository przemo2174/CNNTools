import cv2
from imgaug import augmenters as iaa
from scipy import misc

class ImageModifier:
    def __init__(self, images_paths):
        self.seq = iaa.Sequential([
            iaa.Fliplr(0.5), # horizontally flip 50% of the images
            iaa.GaussianBlur(sigma=(0, 3.0)) # blur images with a sigma of 0 to 3.0
            ])

        self.images_paths = images_paths
        self.modified_images = []        

    def modify_images(self):
        images_data = [misc.imread(image_path) for image_path in self.images_paths]
        print(images_data)

        
