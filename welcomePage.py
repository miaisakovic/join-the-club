from tkinter import *
import customtkinter
from PIL import ImageTk, Image

root = Tk()
root.title ("WELCOME")

welcome_page = ImageTk.PhotoImage(Image.open("welcomePage.png"))
welcome = Label(image = welcome_page)
welcome.pack()

startButton_image = ImageTk.PhotoImage(Image.open ("startButton.png"), Image.ANTIALIAS)
startButton = Button(root, image = startButton_image, borderwidth=0, height = 86, width = 470)
startButton.place(x=115, y=470)

root.mainloop()