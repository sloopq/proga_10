import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Создание основного графика
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

# Начальные значения амплитуд и частот для волн
amp1_init = 1.0
amp2_init = 1.0
freq1_init = 1.0
freq2_init = 1.0

t = np.linspace(0, 2*np.pi, 1000)

# Функция для рассчета суммы волн
def calculate_sum(amp1, amp2, freq1, freq2):
    wave1 = amp1 * np.sin(freq1 * t)
    wave2 = amp2 * np.sin(freq2 * t)
    sum_wave = wave1 + wave2
    return sum_wave

# Функция для обновления графика при изменении параметров
def update(val):
    amp1 = amp_slider1.val
    amp2 = amp_slider2.val
    freq1 = freq_slider1.val
    freq2 = freq_slider2.val
    sum_wave = calculate_sum(amp1, amp2, freq1, freq2)
    ax.clear()
    ax.plot(t, sum_wave)
    plt.draw()

# Создание слайдеров для амплитуд и частот
ax_amp1 = plt.axes([0.25, 0.1, 0.65, 0.03])
amp_slider1 = Slider(ax_amp1, 'Амплитуда 1', 0.1, 2.0, valinit=amp1_init)

ax_amp2 = plt.axes([0.25, 0.05, 0.65, 0.03])
amp_slider2 = Slider(ax_amp2, 'Амплитуда 2', 0.1, 2.0, valinit=amp2_init)

ax_freq1 = plt.axes([0.25, 0.15, 0.65, 0.03])
freq_slider1 = Slider(ax_freq1, 'Частота 1', 0.1, 5.0, valinit=freq1_init)

ax_freq2 = plt.axes([0.25, 0.2, 0.65, 0.03])
freq_slider2 = Slider(ax_freq2, 'Частота 2', 0.1, 5.0, valinit=freq2_init)

amp_slider1.on_changed(update)
amp_slider2.on_changed(update)
freq_slider1.on_changed(update)
freq_slider2.on_changed(update)

plt.show()
