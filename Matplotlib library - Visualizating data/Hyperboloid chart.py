import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4, 4, 100)
y = np.linspace(-4, 4, 100)
x, y = np.meshgrid(x, y)

# Phương trình hyperboloid: -0.3x^2 - 0.3y^2 + z^2 = 1
z = np.sqrt(1 + 0.3*x**2 + 0.3*y**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(x, y, z, cmap='jet', vmin=-5, vmax=5)
ax.plot_surface(x, y, -z, cmap='jet', vmin=-5, vmax=5)  # Vẽ phần dưới của hyperboloid

fig.colorbar(surf, shrink=0.5, aspect=5)

# Gán tiêu đề và nhãn
ax.set_title("Hyperboloid")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x,y)")

plt.show()
