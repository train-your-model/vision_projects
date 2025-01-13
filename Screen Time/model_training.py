# Imports
import os.path
import cv2 as cv
import tensorflow as tf
import numpy as np
import dir_paths


class TrainModel:
    """
    Performs the following tasks:
        1. For the newly added directory with new images, determines the ROI for the images to be cropped.
        2.
    """
    ############## ----------------------------- PARAMETERS -------------------------------####################

    #1 Face Rectangle Coordinates
    rect_coord_dict:dict = dict()

    ################### ----------------------- METHODS ---------------------------------########################
    def face_roi_coord(self):
        """
        Coordinates of the ROI will be in the format: (x,y,w,h)
        :return: A dictionary of image_name and respective facial rectangle coordinates for a given username
        """
        # Loading the required xml classifier file
        haar_class = cv.CascadeClassifier(dir_paths.haar_xml)

        # Reading the Images in the Named Directory
        named_subfolder_path = os.path.join(dir_paths.default_images_path,self.user_name)

        for img in os.listdir(named_subfolder_path):
            gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            # Applying the classifier to the Grayscale Image
            faces_rect = haar_class.detectMultiScale(gray_img, 1.1,9)
            (x, y, w, h) = faces_rect
            TrainModel.rect_coord_dict[img].extend([x,y,w,h])

    def replace_w_roi(self):
        """
        Function to crop the ROI from the original images
        :return: Image with only ROI
        """
        ...

    ################------------------------INITIALIZATION-------------------------------######################
    def __init__(self, user_name):
        self.user_name = user_name