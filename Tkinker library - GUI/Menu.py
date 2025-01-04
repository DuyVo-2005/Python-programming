from tkinter import *
from tkinter import Menu
from tkinter import messagebox

def clicked_New():
    messagebox.showinfo("Notification", "You clicked New")
    
def clicked_Edit():
    messagebox.showinfo("Notification", "You clicked Edit")

def clicked_Help():
    messagebox.showinfo("Notification", "You clicked Help")

window = Tk()
window.title("Welcome to KD app")

# Create the main menu
menu = Menu(window)

# File menu
new_item = Menu(menu)
new_item.add_command(label='New', command=clicked_New)
new_item.add_separator()
new_item.add_command(label='Edit', command=clicked_Edit)
menu.add_cascade(label='File', menu=new_item)

# More menu
new_item2 = Menu(menu)
new_item2.add_command(label='Help', command=clicked_Help)
new_item2.add_command(label='Exit', command=window.quit)
menu.add_cascade(label='More', menu=new_item2)

# Attach menu to the window
window.config(menu=menu)

window.mainloop()