from tkinter import *
import math

root = Tk()
root.title("Công Cụ Tính Toán")

# Các biến
year_solar = StringVar()
year_lunar = StringVar()

fahrenheit = StringVar()
celsius = StringVar()

weight = StringVar()
height = StringVar()
bmi = StringVar()
status = StringVar()


def convert_year():
    solar_year = int(year_solar.get())
    lunar_year = solar_year - 3  # Ví dụ: quy tắc đơn giản
    year_lunar.set(f"Năm âm lịch: {lunar_year}")


def convert_temp():
    f = float(fahrenheit.get())
    c = (f - 32) * 5 / 9
    celsius.set(f"{c:.2f} °C")


def calculate_bmi():
    w = float(weight.get())
    h = float(height.get())
    result = w / (h ** 2)
    bmi.set(f"{result:.2f}")
    if result < 18.5:
        status.set("Gầy")
    elif 18.5 <= result <= 24.9:
        status.set("Bình thường")
    elif 25 <= result <= 29.9:
        status.set("Mập")
    else:
        status.set("Béo phì")


# Giao diện
Label(root, text="Công Cụ", font="15", fg="blue", justify=CENTER).grid(row=0, columnspan=2)

# Chuyển năm dương lịch
Label(root, text="Năm dương lịch:").grid(row=1, column=0)
Entry(root, textvariable=year_solar).grid(row=1, column=1)
Button(root, text="Chuyển đổi", command=convert_year).grid(row=1, column=2)
Label(root, textvariable=year_lunar).grid(row=1, column=3)

# Chuyển độ F sang độ C
Label(root, text="Độ F:").grid(row=2, column=0)
Entry(root, textvariable=fahrenheit).grid(row=2, column=1)
Button(root, text="Chuyển đổi", command=convert_temp).grid(row=2, column=2)
Label(root, textvariable=celsius).grid(row=2, column=3)

# Tính BMI
Label(root, text="Cân nặng (kg):").grid(row=3, column=0)
Entry(root, textvariable=weight).grid(row=3, column=1)

Label(root, text="Chiều cao (m):").grid(row=4, column=0)
Entry(root, textvariable=height).grid(row=4, column=1)

Button(root, text="Tính BMI", command=calculate_bmi).grid(row=5, column=0, columnspan=2)
Label(root, text="BMI:").grid(row=6, column=0)
Label(root, textvariable=bmi).grid(row=6, column=1)

Label(root, text="Tình trạng:").grid(row=7, column=0)
Label(root, textvariable=status).grid(row=7, column=1)

root.mainloop()