from tkinter import *
from PIL import Image, ImageTk

root=Tk()
Label(root,
text="Xin chào! Tui là Khánh Duy",
justify=CENTER,relief=SUNKEN).pack(pady=10)

# Download picture by using Pillow
image = Image.open("KDuyShop.png")
photo = ImageTk.PhotoImage(image)

Label(root, image=photo, relief=RAISED).pack(side=LEFT,padx=5)
root.resizable(height=True,width=True)#permit to resize the size of window
root.minsize(height=300,width=400)

root.mainloop()