from tkinter import *

root = Tk()


def clr():
    a.set("")


def set1():
    a1 = str(a)
    a1 += "1"
    a.set(a1)


def set2():
    a1 = str(a)
    a1 += "2"
    a.set(a1)


def set_add():
    a1 = str(a)
    a1 += "+"
    a.set(a1)


a = StringVar()
Entry(root, textvariable=a, width=9).grid(row=0)

frame1 = Frame(root)
frame1.grid(row=1)
Button(frame1, text="1", command=set1).pack(side=LEFT)
Button(frame1, text="2", command=set2).pack(side=LEFT)
Button(frame1, text="3").pack(side=LEFT)

frame2 = Frame(root)
frame2.grid(row=2)
Button(frame2, text="4").pack(side=LEFT)
Button(frame2, text="5").pack(side=LEFT)
Button(frame2, text="6").pack(side=LEFT)

frame3 = Frame(root)
frame3.grid(row=3)
Button(frame3, text="7").pack(side=LEFT)
Button(frame3, text="8").pack(side=LEFT)
Button(frame3, text="9").pack(side=LEFT)

frame4 = Frame(root)
frame4.grid(row=4)
Button(frame4, text="-").pack(side=LEFT)
Button(frame4, text="0").pack(side=LEFT)
Button(frame4, text="1").pack(side=LEFT)

frame5 = Frame(root)
frame5.grid(row=5)
Button(frame5, text="+", command=set_add).pack(side=LEFT)
Button(frame5, text="-").pack(side=LEFT)
Button(frame5, text="*").pack(side=LEFT)
Button(frame5, text="/").pack(side=LEFT)
Button(frame5, text="=").pack(side=LEFT)

Button(root, text="clr", justify=CENTER, command=clr).grid(row=6)
root.mainloop()
