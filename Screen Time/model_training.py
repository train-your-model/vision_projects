# Imports
import os.path
import uuid
import cv2 as cv
import dir_paths

import tensorflow as tf
from tensorflow import keras


class TrainModel:
    """
    Performs the following tasks:
        1. For the newly added directory with new images, determines the ROI for the images to be cropped.
        2. Trains the model with the image for newly added user-name.
    """
    ####################-----------------------------PARAMETERS-------------------------########################
    ready_for_training:bool = False
    ds_batch_size:int = 10
    ds_img_height:int = 180
    ds_img_width:int = 180

    ################### ----------------------- METHODS ---------------------------------########################
    def crop_img_w_roi(self):
        """
        Function to crop the images taken during along the ROI determined by the classifier
        :return: Cropped images along the ROI
        """
        # Initiating the Classifier
        haar_classification = cv.CascadeClassifier(dir_paths.haar_xml)

        # Full Images
        named_dir = os.path.join(dir_paths.default_images_path,self.user_name)
        full_images = [os.path.join(named_dir, x) for x in os.listdir(named_dir)]

        # Loop
        new_lbl = 'cropped'
        for img in full_images:
            base_img = cv.imread(img)
            gray_img = cv.cvtColor(base_img, cv.COLOR_BGR2GRAY)
            faces_rect = haar_classification.detectMultiScale(gray_img, 1.1, 9)
            for (x, y, w, h) in faces_rect:
                roi_img = base_img[y:y + h, x:x + w]
                roi_img_name = os.path.join(named_dir, new_lbl + '.' + '{}.jpg'.format(str(uuid.uuid1())))
                # Saving the cropped images
                cv.imwrite(roi_img_name, roi_img)

        # Removing the Old Files from the Directory
        for files in full_images:
            os.remove(os.path.join(named_dir, files))

        # Notifying for the Model to be Trained
        TrainModel.ready_for_training = True

    def create_train_dataset(self):
        """
        Function to create a train dataset from the image directory
        """
        train_ds = tf.keras.utils.image_dataset_from_directory(
            directory=os.path.join(dir_paths.default_images_path,self.user_name),
            validation_split=0.2,
            subset="training",
            seed=322,
            image_size=(TrainModel.ds_img_height, TrainModel.ds_img_width),
            batch_size=TrainModel.ds_batch_size
        )
        return train_ds

    def create_val_dataset(self):
        """
        Function to create a validation dataset from the image directory
        """
        val_ds = tf.keras.utils.image_dataset_from_directory(
            directory=os.path.join(dir_paths.default_images_path, self.user_name),
            validation_split=0.2,
            subset="validation",
            seed=322,
            image_size=(TrainModel.ds_img_height, TrainModel.ds_img_width),
            batch_size=TrainModel.ds_batch_size
        )
        return val_ds

    def standardize_layer(self, df):
        normalized_layer = tf.keras.layers.Rescaling(1./255)
        normalized_ds = df.map(lambda x, y: (normalized_layer(x), y))
        return normalized_ds

    def train_model(self):
        ...


    ################------------------------INITIALIZATION-------------------------------######################
    def __init__(self, user_name):
        self.user_name = user_name