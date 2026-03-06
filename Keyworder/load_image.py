from PIL import Image, ImageTk

def Load_image(path, size):
    img = Image.open(path)
    img = img.resize(size)
    return ImageTk.PhotoImage(img)