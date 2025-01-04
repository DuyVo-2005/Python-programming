from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

window = Tk()
window.title("Welcome to KD app")
selected = IntVar()
rad1 = Radiobutton(window,text='First', value=1, variable=selected)
rad2 = Radiobutton(window,text='Second', value=2, variable=selected)
rad3 = Radiobutton(window,text='Third', value=3, variable=selected)
def clicked():
    messagebox.showinfo("Notification", f"Your choice is {selected.get()}")
btn = Button(window, text="Click Me", command=clicked)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
btn.grid(column=3, row=0)
window.mainloop()