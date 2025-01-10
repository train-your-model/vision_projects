import supplementary as sp
import tkinter as tk
from tkinter import messagebox
import images_file as imf

# New User Information Submitted Flag
new_info_sub: int = 0

############### ---------------------------MESSAGES---------------------------------------------###############
def existing_user_warning(name):
    messagebox.showerror("Error", f"User with name: {name} already exists. Try Signing-in")

def new_user_details_submitted():
    messagebox.showinfo("Information", f"Relevant Directories have been created for the New User")

def ask_camera_source():
    user_inp = messagebox.askyesno("Camera Source Confirmation",
                                   "Will you use the integrated camera as the source of the images?")
    if user_inp == 'yes':
        return 0
    else:
        return 1

def get_user_pp():
    user_inp = messagebox.askyesno("User Readiness",
                                   "Are you ready for taking the Profile Picture?")

    if user_inp == 'yes':
        return 1
    else:
        return 0

############# -----------------------------BUTTON COMMANDS---------------------------------------------- ###############
def reg_submit():
    f_name = first_name_entry.get()
    l_name = sur_name_entry.get()
    full_name = f_name + l_name
    global new_info_sub
    new_info_sub += 1
    return full_name

################ ----------------------------WINDOWS----------------------------------------------#############
def main_window():
    "Main Window that pops-up when initiating the file"

    # Initialize
    welcome_page = tk.Tk()

    # Main Window
    welcome_page.title(sp.read_config(ky='root_title', sc='GUI'))
    welcome_page.geometry(sp.read_config(ky='welcome_dimn', sc='GUI'))

    # Greetings Frame
    welcome_frame = tk.Frame(master=welcome_page,
                             height=sp.read_config(ky='greeting_frame_h', sc='GUI-Frames'),
                             width=sp.read_config(ky='greeting_frame_w', sc='GUI-Frames'))
    welcome_frame.pack()

    # Greetings Label
    welcome_lbl = tk.Label(master=welcome_page,
                           text=sp.read_config(ky='greeting_text', sc='GUI-Labels'),
                           bg=sp.read_config(ky='greeting_text_bg', sc='GUI-Labels'),
                           font=sp.read_config(ky='greeting_text_font', sc='GUI-Labels'))
    welcome_lbl.pack()

    # Greetings Buttons
    new_user_btn = tk.Button(master=welcome_page,
                             text=sp.read_config(ky='new_user_btn_txt', sc='GUI-Buttons'),
                             activebackground=sp.read_config(ky='btn_active_background', sc='GUI-Buttons'),
                             disabledforeground=sp.read_config(ky='btn_disabled_foreground', sc='GUI-Buttons'),
                             command=open_registration_window)
    new_user_btn.pack(padx=sp.read_config(ky='register_btn_padx', sc='GUI-Buttons'),
                      pady=sp.read_config(ky='register_btn_pady', sc='GUI-Buttons'))

    return_user_btn = tk.Button(master=welcome_page,
                                text=sp.read_config(ky='returning_user_btn_txt', sc='GUI-Buttons'),
                                activebackground=sp.read_config(ky='btn_active_background', sc='GUI-Buttons'),
                                disabledforeground=sp.read_config(ky='btn_disabled_foreground', sc='GUI-Buttons'))
    return_user_btn.pack(padx=sp.read_config(ky='log-in_btn_padx', sc='GUI-Buttons'),
                         pady=sp.read_config(ky='log-in_btn_pady', sc='GUI-Buttons'))

    # Exit
    welcome_page.mainloop()

# User-Registration Window
def open_registration_window():
    reg_window = tk.Tk()
    reg_window.title(sp.read_config(ky='reg_title', sc='Registration-Window'))
    reg_window.geometry(sp.read_config(ky='reg_dimn', sc='Registration-Window'))

    first_name_var = tk.StringVar()
    sur_name_var = tk.StringVar()

    global first_name_entry
    first_name_lbl = tk.Label(reg_window,
                              text=sp.read_config(ky='f_name-lbl', sc='Registration-Window'),
                              font=sp.read_config(ky='lbl_font', sc='Registration-Window'))
    first_name_entry = tk.Entry(reg_window,
                                textvariable=first_name_var)

    global sur_name_entry
    sur_name_lbl = tk.Label(reg_window,
                            text=sp.read_config(ky='s_name-lbl', sc='Registration-Window'),
                            font=sp.read_config(ky='lbl_font', sc='Registration-Window'))
    sur_name_entry = tk.Entry(reg_window,
                              textvariable=sur_name_var)

    submit_btn = tk.Button(reg_window,
                           text="Submit",
                           command=reg_submit)

    first_name_lbl.grid(row=0, column=0)
    sur_name_lbl.grid(row=3, column=0)
    first_name_entry.grid(row=0, column=3)
    sur_name_entry.grid(row=3, column=3)
    submit_btn.grid(row=6, column=3)

    # Exit
    reg_window.mainloop()

# Window for Taking Images
def images_related_window():
    cam_source_type:int = ask_camera_source()
    ml_pics = imf.TakeImage(user_name=reg_submit(), cam_type=cam_source_type)

    images_window = tk.Tk()
    images_window.title(sp.read_config(ky='img_win_title', sc='Images-Window'))
    images_window.geometry(sp.read_config(ky='img_win_geom', sc='Images-Window'))

    take_ml_images_btn = tk.Button(images_window,
                                   text=sp.read_config(ky='btn1_txt', sc='Images-Window'),
                                   command=get_user_pp)
    take_ml_images_btn.grid(row=6, column=3)

    take_pp_image = tk.Button(images_window,
                                   text=sp.read_config(ky='btn2_txt', sc='Images-Window'),
                                   command=get_user_pp)
    take_pp_image.grid(row=7, column=3)

    user_pp_ready:int = get_user_pp()
    if user_pp_ready == 1:
        ml_pics.take_pp()
    else:
        # Remove the Named folders created during the user registration process
        ...