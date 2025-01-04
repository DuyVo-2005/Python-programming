from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Welcome to KD app")
window.geometry('600x500')
def clicked():
    #Hộp thoại thông tin
    messagebox.showinfo('Message title', 'Message content')
    #Hộp thoại cảnh báo
    messagebox.showwarning('Message title', 'Message content')
    #Hộp thoại báo lỗi
    messagebox.showerror('Message title', 'Message content')
    #Hộp thoại khác
    res = messagebox.askquestion('Message title','Message content')
    res = messagebox.askyesno('Message title','Message content')
    res = messagebox.askyesnocancel('Message title','Message content')
    res = messagebox.askokcancel('Message title','Message content')
    res = messagebox.askretrycancel('Message title','Message content')
btn = Button(window,text='Click here', command=clicked)
btn.grid(column=0,row=0)
window.mainloop()