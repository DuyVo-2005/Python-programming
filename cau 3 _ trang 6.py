from tkinter import *

root = Tk()
root.title("Đăng Nhập")

# Các biến lưu mật khẩu
old_password = StringVar()
new_password = StringVar()
new_password_again = StringVar()


def change_password():
    if new_password.get() == new_password_again.get():
        print("Mật khẩu đã được thay đổi thành công!")
    else:
        print("Mật khẩu mới không khớp!")

Label(root, text="Enter New Password", font="15", justify=CENTER).grid(row=0, columnspan=2)

Label(root, text="Old Password:").grid(row=1, column=0)
Entry(root, textvariable=old_password, width=30, show="*").grid(row=1, column=1)

Label(root, text="New Password: ").grid(row=2, column=0)
Entry(root, textvariable=new_password, width=30, show="*").grid(row=2, column=1)

Label(root, text="Enter New Password Again: ").grid(row=3, column=0)
Entry(root, textvariable=new_password_again, width=30, show="*").grid(row=3, column=1)

frame = Frame(root)
frame.grid(row=4, columnspan=2)

Button(frame, text="OK", command=change_password).pack(side=LEFT)
Button(frame, text="Cancel", command=root.quit).pack(side=LEFT)

root.mainloop()
