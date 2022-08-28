from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("name")
root.geometry("756x491")

top = ImageTk.PhotoImage(Image.open ("background10.png").resize((750,505), Image.ANTIALIAS))
nextpage = ImageTk.PhotoImage(Image.open ("button.png").resize((200,55), Image.ANTIALIAS))


# results label
myLabel = Label(root, image= top, width=750, height=500)
myLabel.grid(row=0,column=0)


# recommendations page button
myButton = Button(root, image= nextpage, height = 55, width = 200)
myButton.place(x=520, y=420)


root.mainloop()