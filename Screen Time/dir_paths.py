# Libraries
import os

# Configuration File Path
config_path = ''

# JSON
record_json_path = os.path.join(os.getcwd(), 'user_creds.json')

# Image Directories Paths
default_base_path = os.path.join(os.getcwd(), 'Tensorflow', 'workspace', 'images')
default_images_path = os.path.join(default_base_path, 'collected_images')
default_pp_path = os.path.join(default_base_path, 'profile_pictures')

# XML File Path
haar_xml = os.path.join(os.getcwd(),'haarcascade_frontalface_default.xml')
