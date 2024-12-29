from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Tree view")
root.geometry("500x500")#chữ x
my_tree = ttk.Treeview(root)

#define columns
my_tree["columns"] = ("Name", "ID", "Favorite fruit")

#Formate columns
my_tree.column("#0", width=120, minwidth=25)
my_tree.column("Name", anchor=W, width=120)
my_tree.column("ID", anchor=CENTER, width=120)
my_tree.column("Favorite fruit", anchor=W, width=120)

#Create headings
my_tree.heading("#0", text="Label", anchor=W,)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Favorite fruit", text="Favorite fruit", anchor=W)

#Add data
my_tree.insert(parent='', index='end', iid=0, text='Parent', values=("Dung",1,"guava"))
my_tree.insert(parent='', index='end', iid=1, text='Parent', values=("Thuy",2,"apple"))
my_tree.insert(parent='', index='end', iid=2, text='Parent', values=("Thao",3,"grape"))
my_tree.insert(parent='', index='end', iid=3, text='Parent', values=("Duy",4,"dragon fruit"))
#iid = items

#Add child
my_tree.insert(parent='', index='end', iid=4, text='Child', values=("Duy Jr",1.2,"durian"))
my_tree.move("4", "3", "0")#move 5 to 4 (0th child of 5)

#Pack to the screen
my_tree.pack(pady=20)

root.mainloop()