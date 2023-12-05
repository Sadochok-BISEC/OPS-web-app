import random

# C = 20 * x1 + 40 * x2
#
# A1 = 22 * x1 + 44 * x2
#
# A2 = 18 * x1 + 36 * x2
#
# 0.6 * (x1 + x2) <= x1
# 0.4 * (x1 + x2) <= x2
# 2 * x1 + 4 * x2 <= 100
# x1, x2 >= 0

# Генерируются случайные значения для переменных x1 и x2,
# удовлетворяющие ограничениям задачи.
# Затем рассчитывается значение целевой функции F для каждой комбинации
# значений x1 и x2 и выбирается комбинация, которая дает оптимальное распределение сырья.

# Целевая функция по умолчанию
def_x1 = 20
def_x2 = 40

# Целевая функция при увеличении цены на 10% - A1
a_up_x1 = 22
a_up_x2 = 44

# Целевая функция при уменьшении цены на 10% - A2
a_down_x1 = 18
a_down_x2 = 36

def monte_carlo(value_x1, value_x2):
    best_x1 = 0
    best_x2 = 0
    best_profit = 0

    iterations = 10000

    for _ in range(iterations):
        x1 = random.uniform(0, 100)  # Случайное значение для x1
        x2 = random.uniform(0, 100)  # Случайное значение для x2

        # Ограничения
        constraint1 = 0.6 * (x1 + x2) <= x1
        constraint2 = 0.4 * (x1 + x2) <= x2
        constraint3 = 2 * x1 + 4 * x2 <= 100

        if constraint1 and constraint2 and constraint3:
            # Целевая функция, которая меняется в зависимости от подпунктов A и B
            profit = value_x1 * x1 + value_x2 * x2

            if profit > best_profit:
                best_profit = profit
                best_x1 = x1
                best_x2 = x2

    return best_x1, best_x2, best_profit

# Default
optimal_def_x1, optimal_def_x2, optimal_def_profit = monte_carlo(def_x1, def_x2)

print("Оптимальное распределение сырья:")
print("П1:", optimal_def_x1, "кг")
print("П2:", optimal_def_x2, "кг")
print("Максимальная выручка:", optimal_def_profit)

# A1
optimal_a1_x1, optimal_a1_x2, optimal_a1_profit = monte_carlo(a_up_x1, a_up_x2)

print("Оптимальное распределение сырья при увеличении цены на 10%:")
print("П1:", optimal_a1_x1, "кг")
print("П2:", optimal_a1_x2, "кг")
print("Максимальная выручка:", optimal_a1_profit)

# A2
optimal_a2_x1, optimal_a2_x2, optimal_a2_profit = monte_carlo(a_down_x1, a_down_x2)

print("Оптимальное распределение сырья при уменьшении цены на 10%:")
print("П1:", optimal_a2_x1, "кг")
print("П2:", optimal_a2_x2, "кг")
print("Максимальная выручка:", optimal_a2_profit)


