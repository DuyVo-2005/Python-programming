from matplotlib import pyplot as plt

# Tạo figure và axes
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])

# Dữ liệu
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23, 17, 35, 29, 48]

# Vẽ biểu đồ tròn
ax.pie(students, labels=langs, autopct="%1.2f%%")  # autopct: Hiển thị phần trăm

# Hiển thị biểu đồ
plt.show()
