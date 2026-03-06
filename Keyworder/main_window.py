from tkinter import Tk, PhotoImage
from main_window_folder.main_element import Main_element

class Main_window:
    def __init__(self):
        self.root_window = Tk()
        self.setup_window()

        self.main_element = Main_element(self.root_window)
        self.main_element.login_button()
        self.main_element.image_title()
        self.main_element.mini_underline_1()
        self.main_element.big_line_1()

        self.main_element.title_keyword()
        self.main_element.typebar_keyword()

        self.main_element.title_sentence()
        self.main_element.typebar_sentence()

        self.main_element.search_typebar()
        self.main_element.search_button_button()
        self.main_element.delete_keyword_sentence_button()

        self.main_element.delete_all_input_typebar()
        self.main_element.add_keyword_sentence_button()
        self.main_element.show_all_keyword_sentence_button()
        self.main_element.clear_output_box_button()
        
        self.main_element.big_border_line_2()

        self.main_element.output_box_information_1()

    def setup_window(self):
        icon = PhotoImage(file="aset/keyworder_icon.png")
        self.root_window.iconphoto(True, icon)

        self.root_window.resizable(width=False, height=False)
        self.root_window.geometry("450x830")
        self.root_window.title('Keyworder')

    def run(self):
        self.root_window.mainloop()

if __name__ == "__main__":
    app = Main_window()
    app.run()