# from tkinter import *
# root = Tk()
# root.title("tk")

# Label(root, text="Cộng trừ nhân chia", font="15", justify=CENTER).grid(
#     row=0, columnspan=2
# )
# a = StringVar()
# b = StringVar()
# x = StringVar()

# Button(root, text="Cộng").grid(row=1, column=0)
# Label(root, text="\tsố a:\t").grid(row=1, column=1)
# Entry(root, textvariable=a, width=35).grid(row=1, column=2)

# Button(root, text="Trừ").grid(row=2, column=0)
# Label(root, text="\tsố b:\t").grid(row=2, column=1)
# Entry(root, textvariable=b, width=35).grid(row=2, column=2)

# Button(root, text="Trừ").grid(row=2, column=0)
# Label(root, text="\tsố b:\t").grid(row=2, column=1)
# Entry(root, textvariable=b, width=35).grid(row=2, column=2)

from tkinter import *

window = Tk()
window.title("Nguyễn Trọng Phúc")
window.geometry("350x200")
a = StringVar()
b = StringVar()
ans = StringVar()
x = StringVar()


def cong():
    ans.set(str(float(a.get()) + float(b.get())))


def tru():
    ans.set(str(float(a.get()) - float(b.get())))


def nhan():
    ans.set(str(float(a.get()) * float(b.get())))


def chia():
    if float(b.get()) == 0:
        ans.set("Lỗi chương trình")
        return
    ans.set(str(float(a.get()) / float(b.get())))


Label(window, text="Cộng trừ nhân chia", fg="black", font="15", justify=CENTER).grid(
    row=0, columnspan=2
)

Button(window, text="Cộng", width=5, command=cong).grid(row=1, column=0)
Label(
    window,
    text="số a: ",
).grid(row=1, column=1)
Entry(window, textvariable=a, width=20).grid(row=1, column=2)

Button(window, text="Trừ", width=5, command=tru).grid(row=2, column=0)
Label(
    window,
    text="số b: ",
).grid(row=2, column=1)
Entry(window, textvariable=b, width=20).grid(row=2, column=2)

Button(window, text="Nhân", width=5, command=nhan).grid(row=3, column=0)
Label(
    window,
    text="Kết quả: ",
).grid(row=3, column=1)
Entry(window, textvariable=ans, width=20).grid(row=3, column=2)

Button(window, text="Chia", width=5, command=chia).grid(row=4, column=0)
Button(window, text="Thoát", command=window.quit).grid(row=4, column=2)

window.mainloop()
