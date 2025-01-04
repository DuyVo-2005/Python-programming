from tkinter import *
root=Tk()
Label(root, text="Muốn thoát à?").pack(pady=10)
Button(root, text="Không").pack(side=RIGHT)
Button(root, text="CÓ",command=root.quit).pack(side=RIGHT)
root.mainloop()