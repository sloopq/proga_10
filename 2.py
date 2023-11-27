import matplotlib.pyplot as plt
import numpy as np

# Создание массива значений времени
t = np.linspace(0, 2 * np.pi, 1000)

# Соотношения частот
frequencies = [(3, 2), (3, 4), (5, 4), (5, 6)]

# Построение фигур Лисажу для каждого соотношения частот
plt.figure(figsize=(10, 8))
for idx, (freq1, freq2) in enumerate(frequencies, 1):
    x = np.sin(freq1 * t)
    y = np.sin(freq2 * t)
    plt.subplot(2, 2, idx)
    plt.plot(x, y)
    plt.title(f'Соотношение частот: {freq1}:{freq2}')
    plt.xlabel('X')
    plt.ylabel('Y')

plt.tight_layout()
plt.show()
