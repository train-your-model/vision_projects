import cv2 as cv
import dir_paths
import time
import uuid
import os

class TakeImage:
    """
    This class performs the following tasks:
        1. Takes the set numbered of images of a registered user for training ML model.
        2. Takes the profile picture of a registered user.
    """

    @property
    def number_of_images(self):
        return self.number_of_images

    @number_of_images.setter
    def number_of_images(self, val):
        print(f"Setting the Number of Images that need to be taken for the Model: {val}")
        self.number_of_images = val

    @number_of_images.deleter
    def number_of_images(self):
        print(f"The Number of images required has been restored to the default value of 10")
        self.number_of_images = 10

    def take_ml_images(self):
        cap = cv.VideoCapture(self.cam_type)
        if not cap.isOpened():
            print('Cannot Open Camera')
            exit()

        label = self.user_name
        print(f"Collecting Images for {label}")
        time.sleep(6)

        for img_num in range(self.number_of_images):
            print(f"Collecting Image No. {img_num}")
            ret, frame = cap.read()
            img_name = os.path.join(self.default_img_folder, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
            cv.imwrite(img_name, frame)
            cv.imshow('frame', frame)
            time.sleep(3)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cap.destroyAllWindows()

    def take_pp(self):
        """
        Takes the image that would be stored as a Profile Picture for a given user
        """
        cap = cv.VideoCapture(self.cam_type)
        if not cap.isOpened():
            print('Cannot Open Camera')
            exit()

        while True:
            label = "Profile Picture" + " " + self.user_name
            print(f'Collecting Image for {label}')
            time.sleep(3)

            ret, frame = cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                exit()

            # Saving the Image
            save_path = os.path.join(dir_paths.default_pp_path, self.user_name)
            cv.imwrite(save_path, frame)


    def __init__(self, user_name, cam_type):
        """
        :param user_name: Full Name given by the user at the time of registration
        :param cam_type: Type of camera being used for taking images. 0 - In-built, 1 - External
        """
        del self.number_of_images
        self.user_name = user_name
        self.cam_type = cam_type
        self.default_img_folder = dir_paths.default_images_path
