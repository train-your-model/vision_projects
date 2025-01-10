import configparser
import os.path
import dir_paths as dp

def read_config(ky, sc):
    """
    :param ky: Key in the relevant section of the 'config.ini' file
    :param sc: Relevant section in the 'config.ini' file
    :return: Value from the file
    """
    parent_path = dp.config_path
    file_name = 'config.ini'

    config = configparser.ConfigParser()
    config.read(os.path.join(parent_path, file_name))
    val = config[sc][ky]
    return val

def remove_named_dirs(user_name):
    """
    In case the user does not wish to continue the registration process, all the named directories
    are removed and the folders are returned to their initial state
    :param user_name: user_name given during the registration process
    """
    ...
