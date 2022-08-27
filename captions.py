from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("name")
root.geometry("756x491")

top = ImageTk.PhotoImage(Image.open ("background10.png"), Image.ANTIALIAS)
nextpage = PhotoImage(file='button.png')


# results label
myLabel = Label(root, image= top)
myLabel.grid(row=0,column=0)


# recommendations page button
myButton = Button(root, image= nextpage, borderwidth=0, height = 80, width = 810)
myButton.place(x=350, y=680)


root.mainloop()