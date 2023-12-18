import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

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

# A.2) Изменение плана выпуска и выручки от продажи при изменении цены на 10%(снижение)
a2_new = [-18, -36]

# Б) Изменение плана выпуска и выручки от продажи при увеличении запаса сырья на 10%
b_ub_new = [-0, 0, 110]

def simplex_found():
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='simplex')
    return res

def simplex_found_a():
    res = linprog(a_new, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='simplex')
    return res

def simplex_found_a2():
    res = linprog(a2_new, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='simplex')
    return res

def simplex_found_b():
    res = linprog(a_new, A_ub=A_ub, b_ub=b_ub_new, bounds=bounds, method='simplex')
    return res

def simplex_draw(x1, x2, picture_name):
    fig, ax = plt.subplots()
    ax.plot([0, 100], [100, 0], 'r-', label='Constraint 1: 0.6(x1+x2) <= x1')
    ax.plot([0, 100], [0, 100], 'g-', label='Constraint 2: 0.4(x1+x2) <= x2')
    ax.plot([0, 50], [25, 0], 'b-', label='Constraint 3: 2x1+4x2 <= 100')
    ax.plot(x1, x2, 'ro', label='Optimal Solution')
    ax.set_xlim([0, 50])
    ax.set_ylim([0, 50])
    ax.legend()
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('Simplex Method')

    return fig.savefig('solutions/static/solutions/new_sol/'+ picture_name +'.png')