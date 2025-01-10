# Imports
import gui
import json_related
import os.path
import dir_paths as dp
import setup_folders as sf

if __name__ == '__main__':
    # Checks the presence of Base Directories
    if not os.path.exists(dp.default_base_path):
        sf.create_base_dir()

    # Main App Window
    gui.main_window()

    # User Registration
    if gui.new_info_sub == 1:
        full_name:str = gui.reg_submit()
        if not os.path.exists(os.path.join(dp.default_pp_path,full_name)):
            sf.create_default_main_img_folder()
            sf.create_named_subfolder(user_name=full_name)
            sf.create_default_main_pp_folder()
            sf.create_named_ppfolder(user_name=full_name)
            gui.new_user_details_submitted()

            # Window for Taking Images for New User
            gui.images_related_window()

        else:
            gui.existing_user_warning(name=full_name)