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

def monte_carlo():
    x1 = random.uniform(0, 100) # случайное значение x1 от 0 до 100
    x2 = random.uniform(0, 100) # случайное значение x2 от 0 до 100

    if 0.6 * (x1 + x2) <= x1 and 0.4 * (x1 + x2) <= x2 and 2 * x1 + 4 * x2 <= 100:
        return True
    else:
        return False

num_trials = 1000000 # количество экспериментов
successful_trials = 0 # количество удачных случаев

for _ in range(num_trials):
    if monte_carlo():
        successful_trials += 1

success_rate = successful_trials / num_trials

print("Удачных случаев:", successful_trials)
print("Вероятность удачного исхода:", success_rate)

optimal_x1 = 0
max_revenue = 0

for _ in range(num_trials):
    x1 = random.uniform(0, 100)
    x2 = random.uniform(0, 100)

    if 0.6 * (x1 + x2) <= x1 and 0.4 * (x1 + x2) <= x2 and 2 * x1 + 4 * x2 <= 100:
        revenue = 20 * x1 + 40 * x2
        if revenue > max_revenue:
            max_revenue = revenue
            optimal_x1 = x1

optimal_x2 = 100 - optimal_x1
num_product_1 = optimal_x1 / 2
num_product_2 = optimal_x2 / 4

print("Оптимальное распределение сырья:")
print("x1 (П1):", optimal_x1, "кг")
print("x2 (П2):", optimal_x2, "кг")
print("Число изготавливаемых видов продукции:")
print("П1:", num_product_1)
print("П2:", num_product_2)

# а2) Изменение цен на 10% снижение
price1_a2 = 20 * 0.9
price2_a2 = 40 * 0.9

revenue_a21 = price1_a2 * num_product_1
revenue_a22 = price2_a2 * num_product_2
total_revenue = revenue_a21 + revenue_a22

print("Изменение цен на 10% снижение:")
print("Выручка от продажи П1:", revenue_a21)
print("Выручка от продажи П2:", revenue_a22)
print("Общая выручка:", total_revenue)

# а1) Изменение цен на 10% увеличение
price_1 = 20 / 0.9
price_2 = 40 / 0.9

revenue_1 = price_1 * num_product_1
revenue_2 = price_2 * num_product_2
total_revenue = revenue_1 + revenue_2

print("Изменение цен на 10% увеличение:")
print("Выручка от продажи П1:", revenue_1)
print("Выручка от продажи П2:", revenue_2)
print("Общая выручка:", total_revenue)

# б) Увеличение суточного запаса на 10%






