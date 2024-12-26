# Hiển thị kích thước màn hình
import tkinter as tk
import pandas as pd
from tkinter import ttk
from tkinter import messagebox
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
messagebox.showinfo("Noted",f"{screen_width}, {screen_height}")
root.mainloop()
