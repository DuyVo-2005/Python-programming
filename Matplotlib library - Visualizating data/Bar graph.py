from matplotlib import pyplot as plt

# Tạo figure và axes
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])

# Dữ liệu
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23, 17, 35, 29, 48]

# Thiết lập các cột của biểu đồ
ax.bar(langs, students)

# Cài đặt ticks và labels
ax.set_xticks(range(len(langs)))  # Cài đặt vị trí ticks (số học)
ax.set_xticklabels(langs)         # Cài đặt nhãn cho các ticks
ax.set_yticks(range(0, 51, 10))   # Cài đặt ticks cho trục y (0-50, cách 10)

# Hiển thị biểu đồ
plt.show()
