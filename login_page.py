from tkinter import *
import customtkinter
from PIL import ImageTk, Image

root = Tk()
root.title ("LOGIN")

login_page = ImageTk.PhotoImage(Image.open("images/login.png"))
login = Label(image = login_page)
login.pack()

loginButton_image = ImageTk.PhotoImage(Image.open ("images/login_button.png"), Image.ANTIALIAS)

loginButton = Button(root, image = loginButton_image, borderwidth=0, height = 67, width = 447)
loginButton.place(x=500, y=780)

handle = Entry(root, width=18, font=('Montserrat 29')) 
handle.insert(0, "INSTAGRAM HANDLE")
handle.place(x = 570, y = 700)

password = Entry(root, width=18, font=('Montserrat 29')) 
password.insert(0, "INSTAGRAM PASSWORD")
password.place(x = 570, y = 608)

username = Entry(root, width=18, font=('Montserrat 29')) 
username.insert(0, "INSTAGRAM USERNAME")
username.place(x = 570, y = 515)

root.mainloop()
