import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt
# monte karlo + graphic

c = np.array([-20, -40])
A_ub = np.array([[-0.4, -0.4], [-0.6, 0], [0, -1]])
b_ub = np.array([0, 0, -100])


def simplex_monte_carlo(c, A_ub, b_ub, N=10000):
    results = []
    for _ in range(N):
        b_ub_mod = b_ub + np.random.uniform(0, 10, len(b_ub))
        res = linprog(c, A_ub=A_ub, b_ub=b_ub_mod)
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

# б) Увеличим суточный запас сырья на 10%:
b_ub_modified = b_ub * 1.1
solution_modified = simplex_monte_carlo(c, A_ub, b_ub_modified)

# graphic
x = np.arange(2)
y1 = solution * c
y2 = solution_modified * c

plt.bar(x, y1, width=0.35, label='Исходные значения')
plt.bar(x+0.35, y2, width=0.35, label='Модифицированные значения')
plt.xlabel('Вид продукции')
plt.ylabel('Выручка от продажи')
plt.title('Сравнение исходных и модифицированных значений')
plt.xticks(x+0.35/2, ['П1', 'П2'])
plt.legend()
plt.show()
