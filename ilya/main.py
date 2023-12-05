import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt
from server.functions.f_simplex import simplex_maximize

# monte karlo + graphic

# без numpy не запускается график
# если хочешь чтобы simplex был идентичен то поменяй значения снизу на как в simplex
#c = np.array([-20, -40])
#A_ub = np.array([[-0.4, -0.4], [-0.6, 0], [0, -1]])
#b_ub = np.array([0, 0, -100])
# Цены продукции П1 и П2
c = [-20, -40]

# Ограничения по объему сбыта продукции П1 и П2
A_ub = [[-0.4, -0.6], [0.6, -1], [2, 4]]
b_ub = [-0, 0, 100]

# Ограничения по знаку переменных x1,x2>=0
x1_bounds = (0, None)
x2_bounds = (0, None)
bounds = [x1_bounds, x2_bounds]

def simplex_monte_carlo(c, A_ub, b_ub, N=10000):
    results = []
    for _ in range(N):
        b_ub_mod = b_ub + np.random.uniform(0, 10, len(b_ub))
        #res = linprog(c, A_ub=A_ub, b_ub=b_ub_mod)
        res = simplex_maximize(c, A_ub, b_ub_mod, bounds)
        results.append(res.x)

    results = np.array(results)
    best_solution = results[np.argmax(np.dot(results, c))]

    return best_solution

solution = simplex_monte_carlo(c, A_ub, b_ub)
print("Оптимальное распределение сырья:")
print("П1:", solution[0] * 100, "кг")
print("П2:", solution[1] * 100, "кг")

# а) Заменим цены на 90% от исходных значений:
c_modified = c * 0.9
solution_modified = simplex_monte_carlo(c_modified, A_ub, b_ub)
print("Изменение цена на 10% снижение")
print("П1:", solution_modified[0] * 100, "кг")
print("П2:", solution_modified[1] * 100, "кг")

c_modified_2 = c / 0.9
solution_modified_2 = simplex_monte_carlo(c_modified, A_ub, b_ub)
print("Изменение цена на 10% увеличение")
print("П1:", solution_modified_2[0] * 100, "кг")
print("П2:", solution_modified_2[1] * 100, "кг")

# б) Увеличим суточный запас сырья на 10%:
b_ub_modified = b_ub * 1.1
solution_modified_b = simplex_monte_carlo(c, A_ub, b_ub_modified)
print("Увеличим суточный запас сырья на 10%:")
print("П1:", solution_modified_b[0] * 100, "кг")
print("П2:", solution_modified_b[1] * 100, "кг")

# graphic
x = np.arange(2)
y1 = solution * c
y2 = solution_modified * c
y3 = solution_modified_2 * c
y4 = solution_modified_b * c

plt.bar(x+0.35, y1, width=0.35, label='Исходные значения')
plt.bar(x+0.70, y2, width=0.35, label='цена на 10% снижение')
plt.bar(x+1.05, y3, width=0.35, label='цена на 10% увеличение')
plt.bar(x+1.40, y4, width=0.35, label='суточный запас сырья на 10%')
plt.xlabel('Вид продукции')
plt.ylabel('Выручка от продажи')
plt.title('Сравнение исходных и модифицированных значений')
plt.xticks(x+0.35/2, ['П1', 'П2'])
plt.legend()
plt.show()
