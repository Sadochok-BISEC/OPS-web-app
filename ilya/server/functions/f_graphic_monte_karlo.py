from scipy.optimize import linprog
import numpy as np
import matplotlib.pyplot as plt

# Определение коэффициентов целевой функции
c = [-20, -40]

# Определение коэффициентов ограничений (левая часть системы неравенств)
A = [[0.4, -0.6],
     [-4, -2]]

# Определение правой части системы неравенств
b = [-60, -100]

# Определение диапазона для переменных
x1_range = (0, 25)
x2_range = (0, 25)

# Генерация случайных значений для переменных
x1_values = np.random.uniform(x1_range[0], x1_range[1], size=[1000])
x2_values = np.random.uniform(x2_range[0], x2_range[1], size=[1000])

# Создание массива для хранения значений целевой функции
objective_values = []

# Вычисление значения целевой функции для каждой комбинации значений переменных
for x1, x2 in zip(x1_values, x2_values):
    objective_values.append(c[0] * x1 + c[1] * x2)

# Построение графика
plt.scatter(x1_values, x2_values, c=objective_values, cmap='viridis')
plt.xlabel('П1')
plt.ylabel('П2')
plt.title('График оптимального распределения сырья')
plt.colorbar(label='Значение целевой функции')
plt.show()

# Решение задачи линейного программирования
result = linprog(c, A_ub=A, b_ub=b, bounds=[x1_range, x2_range])

# Вывод оптимального значения и оптимального распределения сырья
print("Оптимальное значение целевой функции:", -result.fun)
print("Оптимальное распределение сырья:")
print("П1 =", result.x[0])
print("П2 =", result.x[1])
