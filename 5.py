import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Создание данных для графика MSE
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)  # Пример функции MSE

fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_title('3D график MSE')

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, np.log(np.abs(Z) + 1), cmap='viridis')
ax2.set_title('3D график MSE в логарифмическом масштабе')

plt.show()
