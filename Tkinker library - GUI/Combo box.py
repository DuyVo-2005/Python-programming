from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Welcome to HCMUTE app")
window.geometry('350x200')
#Tạo hộp chọn Combobox
combo = Combobox(window)
#Các giá trị của hộp chọn
combo['values']= (1, 2, 3, 4, 5, "Text")
#Thiết lập giá trị được chọn
combo.current(5) #set the selected item
combo.grid(column=0, row=0)
#Lấy giá trị của hộp chọn bằng combo.get()

window.mainloop()