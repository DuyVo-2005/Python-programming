from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Welcome to HCMUTE app")
window.geometry('350x200')
#Thiết lập trạng thái của Checkbox
chk_state = BooleanVar()
chk_state.set(True) #set check state
chk_state2 = BooleanVar()
chk_state2.set(False)
chk_state3 = BooleanVar()
chk_state3.set(True)
#Tạo Checkbox
chk = Checkbutton(window, text='Option 1', var=chk_state)
chk.grid(column=0, row=0)
chk2 = Checkbutton(window, text='Option 2', var=chk_state2)
chk2.grid(column=0, row=1)
chk3 = Checkbutton(window, text='Option 3', var=chk_state3)
chk3.grid(column=0, row=2)
window.mainloop()