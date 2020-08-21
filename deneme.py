from tkinter import *
from PIL import ImageTk, Image
root = Tk()

file = Image.open("Image.jpg")
file = file.resize((100, 100), Image.ANTIALIAS)
Image = ImageTk.PhotoImage(file)  # <---
ImageLabel = Label(root, image=Image)
ImageLabel.image = Image
ImageLabel.grid(row=0, column=0, ipadx=200)
#ImageLabel.grid_rowconfigure(1, weight=2)

l = Label(root, text="I'm a Label")
l.place(anchor=SE)


def takeHashtags():
    str_hashtags = hashtags.get()
    list = str_hashtags.split(",")
    print(list)


root.title("Instagram Automation Bot")
root.geometry("500x400")
hashtags = Entry(root, bd=5)
hashtags.grid()
show = Button(root, bg="light blue", text="show",
              command=lambda: takeHashtags())
show.grid(row=4, column=3)
root.mainloop()
