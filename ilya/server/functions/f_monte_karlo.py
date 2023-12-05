import random

# C = 20 * x1 + 40 * x2
#
# 0.6 * (x1 + x2) <= x1
# 0.4 * (x1 + x2) <= x2
# 2 * x1 + 4 * x2 <= 100
# x1, x2 >= 0

# Генерируются случайные значения для переменных x1 и x2,
# удовлетворяющие ограничениям задачи.
# Затем рассчитывается значение целевой функции F для каждой комбинации
# значений x1 и x2 и выбирается комбинация, которая дает максимальное значение F.

def generate_random_values():
    x1 = random.uniform(0, 100)
    x2 = random.uniform(0, 100)
    return x1, x2

def check_constraints(x1, x2):
    if 0.6 * (x1 + x2) <= x1 \
            and 0.4 * (x1 + x2) <= x2 \
            and 2 * x1 + 4 * x2 <= 100:
        return True
    else:
        return False

def calculate_objective(x1, x2):
    return 20 * x1 + 40 * x2


def monte_carlo_method(iterations):
    max_f = -float('inf')
    opt_x1 = 0
    opt_x2 = 0

    for _ in range(iterations):
        x1, x2 = generate_random_values()

        if check_constraints(x1, x2):
            f = calculate_objective(x1, x2)

            if f > max_f:
                max_f = f
                opt_x1 = x1
                opt_x2 = x2

    return max_f, opt_x1, opt_x2

result = monte_carlo_method(1000000)
print("Максимальное значение целевой функции:", result[0])
print("Оптимальное распределение сырья:")
print("П1:", result[1], "кг")
print("П2:", result[2], "кг")

