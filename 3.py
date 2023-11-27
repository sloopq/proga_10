import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Создание массива значений времени
t = np.linspace(0, 2 * np.pi, 1000)

line, = ax.plot([], [])
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal', adjustable='box')

# Функция инициализации анимации
def init():
    line.set_data([], [])
    return line,

# Функция анимации вращения фигуры Лисажу с изменением соотношения частот
def animate(i):
    x = np.sin(i * t)
    y = np.sin((i * 0.01) * t)  # Изменение соотношения частот от 0 до 1
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)

plt.title('Анимация вращения фигуры Лисажу')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
