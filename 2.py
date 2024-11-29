from tkinter import *
import math

root = Tk()
root.title("PTB2")
# fog ground: màu chữ, font: phông chữ, columnspan: kích thước dàn trải, justify: canh lề

a = StringVar()
b = StringVar()
c = StringVar()
x = StringVar()


def Giai():
    a1 = float(a.get())  # chuyen doi gia tri nhap str -> so
    b1 = float(b.get())
    c1 = float(c.get())
    if a1 == 0:
        if b1 == 0:
            if c1 == 0:
                x.set("Phương trình vô số nghiệm")
            else:
                x.set("Phương trình vô nghiệm")
        else:
            x.set(f"x = {-c1 / b1}")

    delta = b1**2 - 4 * a1 * c1

    if delta < 0:
        x.set("Phương trình vô nghiệm")
    elif delta == 0:
        x.set(f"x = {-b1 / (2 * a1)}")
    else:
        x1 = (-b1 - math.sqrt(delta)) / (2 * a1)
        x2 = (-b1 + math.sqrt(delta)) / (2 * a1)
        x.set(f"x1 = {round(x1, 3)}, x2 = {round(x2, 3)}")


def Tiep():
    # xoa du lieu
    a.set("")  # gan gia tri vao text box
    b.set("")
    c.set("")
    x.set("")


Label(root, text="Vo Le Khanh Duy 23110196", fg="blue", font="15", justify=CENTER).grid(
    row=0, columnspan=2
)
Label(root, text="Hệ số a: ").grid(row=1, column=0)
Entry(root, textvariable=a, width=35).grid(row=1, column=1)  # width: rong 30

Label(root, text="Hệ số b: ").grid(row=2, column=0)
Entry(root, textvariable=b, width=35).grid(row=2, column=1)

Label(root, text="Hệ số c: ").grid(row=3, column=0)
Entry(root, textvariable=c, width=35).grid(row=3, column=1)

frame = Frame(root)

frame.grid(row=4, columnspan=2)

Button(frame, text="Giải", command=Giai).pack(side=LEFT)  # sát nhau
Button(frame, text="Tiếp", command=Tiep).pack(side=LEFT)  # sát nhau
Button(frame, text="Thoát", command=root.quit).pack(side=LEFT)  # sát nhau

Label(root, text="Kết quả: ").grid(row=5, column=0)
Entry(root, textvariable=x, width=35).grid(row=5, column=1)

root.mainloop()
