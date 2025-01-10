import dir_paths as dp
import os.path


def create_base_dir():
    """
    This function creates the base directory
    """
    if not os.path.exists(dp.default_base_path) and os.name == 'nt':
        return os.makedirs(dp.default_base_path)

def create_default_main_img_folder():
    """
    This function creates the directory for the collected images are to be stored for the training of the ML model
    """
    if not os.path.exists(dp.default_images_path) and os.name == 'nt':
        return os.mkdir(dp.default_images_path)

def create_named_subfolder(user_name):
    """
    This function creates a named sub-folder based on the user defined label name.
    """
    parent_dir = dp.default_images_path
    path = os.path.join(parent_dir, user_name)
    return os.mkdir(path)

def create_default_main_pp_folder():
    """
    This function creates the directory for the profile pictures are to be stored for DB purposes
    """
    if not os.path.exists(dp.default_pp_path) and os.name == 'nt':
        return os.mkdir(dp.default_pp_path)

def create_named_ppfolder(user_name):
    """
    This function creates the folder for storing profile picture associated with the user name
    :param user_name: Value given by the user as their name
    """
    path = os.path.join(dp.default_pp_path, user_name)
    return os.mkdir(path)