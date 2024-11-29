from tkinter import *
import math

root = Tk()
root.title("PTB1")
# fog ground: màu chữ, font: phông chữ, columnspan: kích thước dàn trải, justify: canh lề

a = StringVar()
b = StringVar()
x = StringVar()


def Giai():
    a1 = float(a.get())  # chuyen doi gia tri nhap str -> so
    b1 = float(b.get())
    if a1 == 0 and b1 == 0:
        x.set("Phương trình vô số nghiệm")
    elif a1 == 0 and b1 != 0:
        x.set("Phương trình vô nghiệm")
    else:
        x.set(f"x = {-b1 / a1}")


def Tiep():
    # xoa du lieu
    a.set("")  # gan gia tri vao text box
    b.set("")
    x.set("")


Label(root, text="Phương Trình Bậc 1", fg="red", font="15", justify=CENTER).grid(
    row=0, columnspan=2
)
Label(root, text="Hệ số a: ").grid(row=1, column=0)
Entry(root, textvariable=a, width=35).grid(row=1, column=1)  # width: rong 35

Label(root, text="Hệ số b: ").grid(row=2, column=0)
Entry(root, textvariable=b, width=35).grid(row=2, column=1)

frame = Frame(root)

frame.grid(row=3, columnspan=2)

Button(frame, text="Giải", command=Giai).pack(side=LEFT)  # sát nhau
Button(frame, text="Tiếp", command=Tiep).pack(side=LEFT)  # sát nhau
Button(frame, text="Thoát", command=root.quit).pack(side=LEFT)  # sát nhau

Label(root, text="Kết quả: ").grid(row=4, column=0)
Entry(root, textvariable=x, width=35).grid(row=4, column=1)

root.mainloop()
