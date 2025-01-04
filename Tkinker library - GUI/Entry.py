from tkinter import *
from tkinter import messagebox
def show_name():
    global e
    messagebox.showinfo("Notification",f"Your name is {e.get()}")
root=Tk()
Label(root, text="Enter your name:").pack(side=LEFT, padx=5, pady=10)
e = StringVar()
Entry(root, width=40, textvariable=e).pack(side=LEFT)
e.set("Võ Lê Khánh Duy")
Button(root,text="Say OK",command=show_name).pack(side=LEFT)
root.mainloop()