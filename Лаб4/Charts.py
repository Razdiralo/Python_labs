import numpy as np
import matplotlib.pyplot as plt

# Функция из первой задачи
def calculate_a(x, y):
    f_x = x**2  # f(x) = x^2
    if x * y > 0:
        return (f_x + y) ** 2 - np.sqrt(abs(f_x * y))  # Учитываем abs() для корректности
    elif x * y < 0:
        return (f_x + y) ** 2 + np.sqrt(abs(f_x * y))
    else:  # x * y == 0
        return (f_x + y) ** 2 + 1

# Данные для графиков
x = np.linspace(-5, 5, 500)  # Диапазон значений x
y = np.linspace(-5, 5, 500)  # Диапазон значений y

# Вычисляем значения для функции calculate_a
a_values = np.array([calculate_a(xi, yi) for xi, yi in zip(x, y)])

# Вторая функция для демонстрации (например, синус)
sin_values = np.sin(x)

# Создаем фигуру и оси
fig, ax1 = plt.subplots(figsize=(10, 6))  # Основная фигура

# --- Первая ось Y ---
ax1.plot(x, a_values, label="Функция calculate_a(x, y)", color='b', linewidth=2)
ax1.set_xlabel("Значения x", fontsize=12)
ax1.set_ylabel("Значения a(x, y)", color='b', fontsize=12)
ax1.tick_params(axis='y', labelcolor='b')
ax1.grid(True, linestyle='--', alpha=0.5)

# --- Вторая ось Y ---
ax2 = ax1.twinx()  # Вторая ось Y
ax2.plot(x, sin_values, label="Функция sin(x)", color='r', linestyle='--')
ax2.set_ylabel("Значения sin(x)", color='r', fontsize=12)
ax2.tick_params(axis='y', labelcolor='r')

# --- Легенда и аннотация ---
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9), fontsize=10)
ax1.annotate("Точка пересечения",
             xy=(0, calculate_a(0, 0)),  # Координаты
             xytext=(-2, 50),  # Текст аннотации
             arrowprops=dict(facecolor='black', shrink=0.05))

# --- Заголовок ---
plt.title("График функции calculate_a(x, y) и sin(x)", fontsize=14)

# Сохраняем график
plt.savefig("combined_plot.png", dpi=300)
plt.savefig("combined_plot.pdf", dpi=300)

# Показываем график
plt.show()
