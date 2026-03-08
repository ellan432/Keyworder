from login_window_folder.login_frame import Login_frame
from tkinter import *
from aset import Aset
from tkinter import filedialog as fd
from PIL import Image,ImageTk

class Login_element:
    def __init__(self, login_win, root_window, login_btn):
        self.login_win = login_win
        self.login_frame = Login_frame(login_win)
        self.root_window = root_window
        self.login_btn = login_btn
        self.aset = Aset()

#profile picture label
    def profile_picture(self):
        self.picture_label = Label(self.login_frame.frame_pp,
                text=" ",
                bg="#CCCCCC",
                relief="sunken",
                padx=65,
                pady=55,
                bd=2,
                image=self.aset.default_pp_large)
        self.picture_label.grid(row=0, column=0, pady=(20,5))

#button to choose profile picture
    def edit_pp_button(self):
        edit_pp_btn = Button(self.login_frame.frame_pp,
                             text="edit profile",
                             padx=5,
                             pady=1,
                             command=self.open_file)
        edit_pp_btn.grid(row=1, column =0)

#button commnad so it can open file to choose profile picture
    def open_file(self):
        self.picture_file_path = fd.askopenfilename(
            title="choose profile picture",
            filetypes= [('Image', '*.jpg *.png *.jpeg')],
            initialdir='/'
        )

        try:
            if self.picture_file_path == " " or self.picture_file_path == "()":  
                print(f"{self.picture_file_path} <== file path value")
                return None

            else:
                print(f"{self.picture_file_path} <== file path value")
                self.load_picture = Image.open(self.picture_file_path)
                
                self.load_picture = self.load_picture.resize((130,130))
                self.render_picture = ImageTk.PhotoImage(self.load_picture)
                self.picture_label.config(image=self.render_picture)
                self.picture_label.render_picture = self.render_picture

        except AttributeError:
            print("you not enter any file")
            return self.picture_label

#change login button to show profile picture
    def change_login_button(self):
        try:
            self.load_picture = self.load_picture.resize((20,20))
            self.render_picture = ImageTk.PhotoImage(self.load_picture)
            self.login_btn.config(image=self.render_picture, compound="right")
            self.login_btn.render_picture_small = self.render_picture

        except AttributeError:
            return self.login_btn

    
#class for login input menu template
    class login_input_menu:
        def __init__(self, frame, image, config):

            self.frame = frame
            self.image = image
            self.text = config.get("text", "")
            self.width_login_typebar = config.get("width typebar", 33)
            self.row_title_typebar = config.get("row title typebar", 0)
            self.column_title_typebar = config.get("column title typebar", 0)
            self.row_login_typebar = config.get("row typebar", 0)
            self.column_login_typebar = config.get("column typebar", 0)
            self.column_bacspace_button =  config.get("column backspace", 0)
            self.title_bgcolor = config.get("title bgcolor", "#cccccc")
            self.typebar_bgcolor = config.get("typebar bgcolor", "#d7d7d7")

        def title_input(self):
            self.title_typebar = Label(self.frame,
                          text=self.text,
                          bg=self.title_bgcolor)
            self.title_typebar.grid(row=self.row_title_typebar, column=self.column_title_typebar, sticky="w")

        def login_input_typebar(self):
            self.input_typebar = Entry (self.frame,
                                        bg=self.typebar_bgcolor,
                                        width=self.width_login_typebar)
            self.input_typebar.grid(row=self.row_login_typebar, column=self.column_login_typebar)

        def delete_typebar_button(self):
            self.delete_typebar_btn = Button(self.frame,
                                             image=self.image,
                                             pady=1,
                                             command=self.delete_input)
            self.delete_typebar_btn.image_ref = self.image
            self.delete_typebar_btn.grid(row=self.row_login_typebar, column=self.column_bacspace_button)

        def delete_input(self):
            self.input_typebar.delete(0,END)

#username input menu
    def username_menu(self):
        self.config = {
            "text" : "Username",
            "row title typebar" : 0,
            "column title typebar" : 0,
            "row typebar" : 1,
            "column typebar" : 0,
            "column backspace" : 1}
        
        self.username_input = self.login_input_menu(self.login_frame.frame_input_data, self.aset.backspace_img, self.config)
        self.username_input.title_input()
        self.username_input.login_input_typebar()
        self.username_input.delete_typebar_button()

#email input menu
    def email_menu(self):
        self.config = {
            "text" : "Email",
            "row title typebar" : 2,
            "column title typebar" : 0,
            "row typebar" : 3,
            "column typebar" : 0,
            "column backspace" : 1}
        
        self.email_input = self.login_input_menu(self.login_frame.frame_input_data, self.aset.backspace_img, self.config)
        self.email_input.title_input()
        self.email_input.login_input_typebar()
        self.email_input.delete_typebar_button()

#email warn if email input not falid
    def email_warn(self):
        self.email_warn_message = Label(self.login_frame.frame_input_data,
                                   text='Please enter valid email adress !',
                                   fg="#cccccc",
                                   bg='#cccccc')
        self.email_warn_message.grid(row=4, column=0)

#password input
    def password_menu(self):
        self.config = {
            "text" : "Password",
            "row title typebar" : 5,
            "column title typebar" : 0,
            "row typebar" : 6,
            "column typebar" : 0,
            "column backspace" : 1}
        
        self.password_input = self.login_input_menu(self.login_frame.frame_input_data, self.aset.backspace_img, self.config)
        self.password_input.title_input()
        self.password_input.login_input_typebar()
        self.password_input.delete_typebar_button()

#command for check if there any input value for username
    def empty_username_warn(self):
        self.username_value = self.username_input.input_typebar.get()
        self.username_value.strip()

        if self.username_value:
            self.username_input.title_typebar.config(image="")
        else:
            self.username_input.title_typebar.config(image=self.aset.red_dots, compound="left")

#command for check if there any input value for email
    def empty_email_warn(self):
        self.email_value = self.email_input.input_typebar.get()
        self.email_value.strip()

        if self.email_value:
            self.email_input.title_typebar.config(image="")
        else:
            self.email_input.title_typebar.config(image=self.aset.red_dots, compound="left")

#command for check if there any input value for password
    def empty_password_warn(self):
        self.password_value = self.password_input.input_typebar.get()
        self.password_value.strip()

        if self.password_value:
            self.password_input.title_typebar.config(image="")
        else:
            self.password_input.title_typebar.config(image=self.aset.red_dots, compound="left")
        
#to check is that empty input, if yes warn will apear, if no, login window will destroy and refeal the main window
    def show_main_window(self):
        self.email_value = self.email_input.input_typebar.get()
        if "@email.com" in self.email_value or "@gmail.com" in self.email_value:
            self.email_warn_message.config(fg="#cccccc")
            if self.username_value and self.email_value and self.password_value:
                image_pp_default = self.aset.default_pp_icon
                self.login_win.after(1000, lambda: self.login_win.destroy())#destroy the login window after 1 second
                self.login_btn.config(text=self.username_value, image=image_pp_default, compound="right")
                self.login_btn.image_default = image_pp_default
                self.root_window.after(1000, lambda: self.root_window.deiconify())#main window apear after 1 second
                
        else:
            self.email_warn_message.config(fg="#FF0000")
    
#submit button
    def submit_button(self):
        submit_btn = Button(self.login_frame.submit_frame,
                            text="Log in",
                            padx=5,
                            pady=2,
                            bd=1,
                            command=lambda:[self.empty_username_warn(), self.empty_email_warn(), self.empty_password_warn(), self.show_main_window(), self.change_login_button()])
        submit_btn.grid(row=0, column=0, pady=(10,0))