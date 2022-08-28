from operator import truediv
from tkinter import *
from PIL import ImageTk
from PIL import Image as Image2

root = Tk()
root.title ("JOIN THE CLUB!")
root.geometry("756x491")


img = Image("photo", file="images/icon.png")
root.call('wm', 'iconphoto', root._w, img)


counter = 0


# Backgrounds
welcome_page = ImageTk.PhotoImage(Image2.open("images/welcome_page.png").resize((750,505), Image2.ANTIALIAS))
login_page = ImageTk.PhotoImage(Image2.open("images/login.png").resize((750,505), Image2.ANTIALIAS))
captions_page = ImageTk.PhotoImage(Image2.open("images/captions_page.png").resize((750,505), Image2.ANTIALIAS))
other_clubs_page = ImageTk.PhotoImage(Image2.open("images/other_clubs_page.png").resize((750,505), Image2.ANTIALIAS))

backgrounds = [welcome_page, login_page, captions_page, other_clubs_page]


# Buttons that lead to other pages
start_button_img = ImageTk.PhotoImage(Image2.open("images/start_button.png").resize((280,65), Image2.ANTIALIAS))
login_button_img = ImageTk.PhotoImage(Image2.open("images/login_button.png").resize((190,35), Image2.ANTIALIAS))
other_clubs_button_img = ImageTk.PhotoImage(Image2.open("images/captions_button.png").resize((195,45), Image2.ANTIALIAS))

buttons = [start_button_img, login_button_img, other_clubs_button_img]


# Buttons for other clubs
blueprint_button = ImageTk.PhotoImage(Image2.open("images/blueprint_icon.png").resize((200,200), Image2.ANTIALIAS))
wics_button = ImageTk.PhotoImage(Image2.open("images/wics_icon.png").resize((200,200), Image2.ANTIALIAS))
techplus_button = ImageTk.PhotoImage(Image2.open("images/techplus_icon.png").resize((200,200), Image2.ANTIALIAS))


def next_page():
    global counter
    global current_background
    global current_button
    global handle
    global password
    global username

    counter = counter + 1

    current_background.place_forget()
    current_button.pack_forget()

    # Display new background
    current_background = Label(image = backgrounds[counter], width=750, height=500)
    current_background.place(x=0, y=0)

    # Widgets for the login page
    if counter == 1:
        current_button = Button(root, image = buttons[counter], borderwidth=0, height=35, width=150, command=next_page)
        current_button.pack(side=BOTTOM, padx=200, pady=16)

        handle = Entry(root, width=21, font=('Montserrat 16'), justify="center") 
        handle.insert(0, "Club Instagram Handle")
        handle.pack(side=BOTTOM, padx=200, pady=15)

        password = Entry(root, width=21, font=('Montserrat 16'), justify="center") 
        password.insert(0, "Instagram Password")
        password.pack(side=BOTTOM, padx=200, pady=0)

        username = Entry(root, width=21, font=('Montserrat 16'), justify="center") 
        username.insert(0, "Instagram Username")
        username.pack(side=BOTTOM, padx=200, pady=15)

    # Widgets for the captions page
    if counter == 2:
        current_button = Button(root, image = buttons[counter], borderwidth=0, height=35, width=185, command=next_page)
        current_button.pack(side=BOTTOM, anchor="e", padx=25, pady=25)

        handle.pack_forget()
        password.pack_forget()
        username.pack_forget()

    # Widgest for the other clubs page
    if counter == 3:
        # Blueprint option button
        Option1 = Button(root, image = blueprint_button, height=185, width=185)
        Option1.place(x=100, y=145)

        # WICS option button
        Option2 = Button(root, image = wics_button, height=185, width=185)
        Option2.place(x=300, y=145)

        # TechPlus option button
        Option3 = Button(root, image = techplus_button, height=185, width=185)
        Option3.place(x=500, y=145)


# Display Welcome Page
current_background = Label(image = backgrounds[counter], width=750, height=500)
current_background.place(x=0, y=0)

current_button = Button(root, image = buttons[counter], borderwidth=0, height=65, width=280, command=next_page)
current_button.pack(side=BOTTOM, anchor="w", padx=50, pady=100)


root.mainloop()
