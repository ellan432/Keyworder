from load_image import Load_image

class Aset:
    def __init__(self):
        
        self.title_img = Load_image("aset/icon_and_name.png",(250,70))
        self.backspace_img = Load_image('aset/backspace.png',(20,20))
        self.default_pp_icon = Load_image("aset/default_pp.png", (20,20))
        self.default_pp_large = Load_image("aset/default_pp.png", (130,130))
        self.down_arow_icon = Load_image("aset/downarow.png",(20,20))
        self.search_img = Load_image('aset/search.png',(20,20))
        self.trash_icon = Load_image("aset/trash.png",(20,20))
        self.red_cross_img =Load_image('aset/cross.png', (20,20))
        self.plus_img = Load_image('aset/plus.png',(20,20))
        self.show_all_img = Load_image('aset/show_all.png',(20,20))
        self.show_all_img = Load_image('aset/show_all.png', (20,20))
        self.clear_img = Load_image('aset/mini_broom.png', (20,20))
        self.red_dots = Load_image('aset/red_dot.png', (13,13))

        self.underline_sign = '_'
        self.equal_sign = '='
        self.strip_sign = "-"

        self.double = 1.0
        self.single = 0