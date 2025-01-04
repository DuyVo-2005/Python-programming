#from tkinter import filedialog
#file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
#dir = filedialog.askdirectory()

## Chỉ định thư mục ban đầu cho hộp thoại tệp bằng chỉ định initialdir
from tkinter import filedialog
from os import path
file = filedialog.askopenfilename(initialdir= path.dirname(__file__))