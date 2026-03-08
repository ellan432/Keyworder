from tkinter import Toplevel
from login_window_folder.login_element import Login_element

class Login_window:
    def __init__(self, parent, login_btn):
        self.parent = parent
        self.login_win = Toplevel(parent) #to make login_window become child to parent window (main window)
        self.login_btn = login_btn
        self.login_window_setup()

        self.login_element = Login_element(self.login_win, parent, login_btn)
        self.login_element.profile_picture()
        self.login_element.edit_pp_button()

        self.login_element.username_menu()

        self.login_element.email_menu()
        self.login_element.email_warn()

        self.login_element.password_menu()

        self.login_element.submit_button()
    
    def login_window_setup(self):
        self.login_win.geometry("350x500")
        self.login_win.title("Log In")
        self.login_win.resizable(height=False, width=False)