from tkinter import Frame, SUNKEN

class Login_frame:
    def __init__(self, login_win):
        self.login_win = login_win

        #( FRAME PP)
        self.frame_pp = Frame(self.login_win)
        self.frame_pp.pack(padx=(0,0), pady=(0,0))

        #( FRAME INPUT DATA)
        self.frame_input_data = Frame(self.login_win, relief=SUNKEN, bd=2, bg="#cccccc", padx=5, pady=5)
        self.frame_input_data.pack(padx=(0,0), pady=(10,0))

        self.submit_frame = Frame(self.login_win)
        self.submit_frame.pack(padx=(0,0), pady=(0,0))