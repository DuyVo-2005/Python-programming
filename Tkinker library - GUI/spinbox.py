# Giá trị spinbox trong đoạn [from_ ; to]
from tkinter import *
window = Tk()
window.title("Welcome to KD app")
window.geometry('600x500')
# Tạo spinbox có chiều rộng 8, giá trị từ 0 đến 10
spin = Spinbox(window, from_=0, to=10, width=8)
spin.grid(column=0,row=0)
window.mainloop()

# Liệt kê các giá trị của spinbox
#from tkinter import *
#window = Tk()
#window.title("Welcome to KD app")
#window.geometry('600x500')
## spinbox chỉ gồm có 3 giá trị là 3, 8 và 11
#spin = Spinbox(window, values=(3, 8, 11), width=5)
#spin.grid(column=0,row=0)
#window.mainloop()

#from tkinter import *
#window = Tk()
#window.title("Welcome to KD app")
#window.geometry('600x500')
#var =IntVar()
## Đặt giá trị mặc định là 99
#var.set(99)
#spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
#spin.pack(pady=10, padx= 10)
#window.mainloop()