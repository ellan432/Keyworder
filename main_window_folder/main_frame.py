from tkinter import Frame, NE 

class Main_frame:
    def __init__(self):

        #( FRAME TOP )
        self.frame_top = Frame()
        self.frame_top.pack(pady=(10,0), padx=(0,10), anchor=NE)

        #( FRAME TITLE )
        self.frame_title = Frame()
        self.frame_title.pack(pady=(0,0), padx=(0,160))

        #( FRAME UNDER TITLE )
        self.frame_under_title = Frame()
        self.frame_under_title.pack(pady=(0,0), padx=(0,0))

        #( FRAME BIG UNDERLINE 1 )
        self.frame_big_line1 = Frame()
        self.frame_big_line1.pack(pady=(0,0), padx=(0,0))

        #( FRAME INPUT )
        self.frame_input = Frame( bg="#cccccc", bd=2, relief="sunken")
        self.frame_input.pack(pady=(0,0), padx=(0,0))


        #( FRAME SEARCH )
        self.frame_search = Frame()
        self.frame_search.pack(pady=(5,0),padx=(0,0))

        #( FRAME 4 )
        self.frame_menu_button = Frame()
        self.frame_menu_button.pack(pady=(0,0),padx=(0,0))

        #( FRAME 5 )
        self.frame_big_line2 = Frame()
        self.frame_big_line2.pack(pady=(0,0),padx=(0,0))

        #( FRAME 6 )
        self.frame_outputbox = Frame()
        self.frame_outputbox.pack(pady=(0,0),padx=(0,0))