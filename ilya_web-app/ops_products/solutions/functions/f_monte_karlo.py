import numpy as np
from scipy.optimize import linprog

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

# Цены продукции П1 и П2
c = np.array([-20, -40])

# Ограничения по объему сбыта продукции П1 и П2
A_ub = np.array([[-0.4, -0.6], [0.6, -1], [2, 4]])
b_ub = np.array([-0, 0, 100])

# Ограничения по знаку переменных x1,x2>=0
x1_bounds = (0, None)
x2_bounds = (0, None)
bounds = [x1_bounds, x2_bounds]

# A) Изменение плана выпуска и выручки от продажи при изменении цены на 10%(увеличение)
a_new = [-22, -44]
c_modified_2 = c / 0.9

# A.2) Изменение плана выпуска и выручки от продажи при изменении цены на 10%(снижение)
a2_new = [-18, -36]
c_modified_1 = c * 0.9

# Б) Изменение плана выпуска и выручки от продажи при увеличении запаса сырья на 10%
b_ub_new = [-0, 0, 110]
b_ub_modified = b_ub * 1.1

N=10000

def monte_carlo_found():
    results = []
    for _ in range(N):
        b_ub_mod = b_ub + np.random.uniform(0, 10, len(b_ub))
        res = linprog(c, A_ub=A_ub, b_ub=b_ub_mod,  method='simplex')
        results.append(res.x)

    results = np.array(results)
    best_solution = results[np.argmax(np.dot(results, c))]

    return best_solution

def monte_carlo_found_a():
    results = []
    for _ in range(N):
        b_ub_mod = b_ub + np.random.uniform(0, 10, len(b_ub))
        res = linprog(c_modified_2, A_ub=A_ub, b_ub=b_ub_mod,  method='simplex')
        results.append(res.x)

    results = np.array(results)
    best_solution = results[np.argmax(np.dot(results, c))]

    return best_solution

def monte_carlo_found_b():
    results = []
    for _ in range(N):
        b_ub_mod = b_ub + np.random.uniform(0, 10, len(b_ub))
        res = linprog(c, A_ub=A_ub, b_ub=b_ub_modified,  method='simplex')
        results.append(res.x)

    results = np.array(results)
    best_solution = results[np.argmax(np.dot(results, c))]

    return best_solution