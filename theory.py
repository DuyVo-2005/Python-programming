# # # # # # from tkinter import *

# # # # # # top = Tk()
# # # # # # top.title("Hello Duy app")
# # # # # # top.geometry("500x300")
# # # # # # top.resizable(height=True, width=True)
# # # # # # top.minsize(height=300, width=400)


# # # # # # def makecenter(root):
# # # # # #     root.update_idletasks()
# # # # # #     width = root.winfo_width()
# # # # # #     height = root.winfo_height()
# # # # # #     x = (root.winfo_screenwidth() // 2) - (width // 2)
# # # # # #     y = (root.winfo_screenheight() // 2) - (height // 2)
# # # # # #     root.geometry("{}x{}+{}+{}".format(width, height, x, y))


# # # # # # makecenter(top)
# # # # # # top.mainloop()

# # # # # # from tkinter import *

# # # # # # root = Tk()
# # # # # # Label(root, text="Xin chào! Tui là tkinter", justify=CENTER, relief=SUNKEN).pack(
# # # # # #     pady=10
# # # # # # )
# # # # # # photo = PhotoImage(
# # # # # #     file="C:\\Users\\HP\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-11-21 214458.png"
# # # # # # )
# # # # # # Label(root, image=photo, relief=RAISED).pack(side=LEFT, padx=5)
# # # # # # root.resizable(height=True, width=True)
# # # # # # root.minsize(height=300, width=400)
# # # # # # root.mainloop()

# # # # # # from tkinter import *

# # # # # # root = Tk()
# # # # # # Label(root, text="Muốn thoát hả?").pack(pady=10)
# # # # # # Button(root, text="Không").pack(side=RIGHT)
# # # # # # Button(root, text="CÓ", command=root.quit).pack(side=RIGHT)
# # # # # # root.mainloop()

# # # # # # lấy giá trị e.get()
# # # # # # gán giá trị e.set()

# # # # # from tkinter import *

# # # # # root = Tk()
# # # # # Label(root, text="Enter your name:").pack(side=LEFT, padx=5, pady=10)
# # # # # e = StringVar()
# # # # # Entry(root, width=40, textvariable=e).pack(side=LEFT)
# # # # # e.set("Trần Duy Thanh")
# # # # # Button(root, text="Say OK").pack(side=LEFT)
# # # # # root.mainloop()

# # # # from tkinter import *
# # # # from tkinter.ttk import *

# # # # window = Tk()
# # # # window.title("Welcome to HCMUTE app")
# # # # window.geometry("350x200")
# # # # # Tạo hộp chọn Combobox
# # # # combo = Combobox(window)
# # # # # Các giá trị của hộp chọn
# # # # combo["values"] = (1, 2, 3, 4, 5, "Text")
# # # # # Thiết lập giá trị được chọn
# # # # combo.current(1)  # set the selected item
# # # # combo.grid(column=0, row=0)
# # # # # Lấy giá trị của hộp chọn bằng combo.get()
# # # # # window.mainloop()

# # # from tkinter import *
# # # from tkinter.ttk import *

# # # window = Tk()
# # # window.title("Welcome to HCMUTE app")
# # # selected = IntVar()
# # # rad1 = Radiobutton(window, text="First", value=1, variable=selected)
# # # rad2 = Radiobutton(window, text="Second", value=2, variable=selected)
# # # rad3 = Radiobutton(window, text="Third", value=3, variable=selected)


# # # def clicked():
# # #     print(selected.get())


# # # btn = Button(window, text="Click Me", command=clicked)
# # # rad1.grid(column=0, row=0)
# # # rad2.grid(column=1, row=0)
# # # rad3.grid(column=2, row=0)
# # # btn.grid(column=3, row=0)
# # # window.mainloop()

# # from tkinter import *
# # from tkinter import scrolledtext

# # window = Tk()
# # window.title("Welcome to HCMUTE app")
# # window.geometry("350x200")
# # txt = scrolledtext.ScrolledText(window, width=40, height=10)
# # txt.grid(column=0, row=0)
# # window.mainloop()

# from tkinter import *
# from tkinter import messagebox

# window = Tk()
# window.title("Welcome to HCMUTE app")
# window.geometry("350x200")


# def clicked():
#     messagebox.showinfo("Message title", "Message content")


# btn = Button(window, text="Click here", command=clicked)
# btn.grid(column=0, row=0)
# window.mainloop()

from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Welcome to LikeGeeks app")
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text="First")
tab_control.add(tab2, text="Second")
lbl1 = Label(tab1, text="label1")
lbl1.grid(column=0, row=0)
lbl2 = Label(tab2, text="label2")
lbl2.grid(column=0, row=0)
tab_control.pack(expand=1, fill="both")
window.mainloop()
