import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

# Создание массива значений x
x = np.linspace(-1, 1, 100)

# Задание степеней полиномов Лежандра
degrees = [1, 2, 3, 4, 5, 6, 7]

# Построение графиков полиномов Лежандра различных степеней
for degree in degrees:
    y = legendre(degree)(x)
    plt.plot(x, y, label=f'n = {degree}')

# Заголовок и легенда графика
plt.title('Полиномы Лежандра')
plt.legend(loc='upper right')

# Отображение графика
plt.show()
