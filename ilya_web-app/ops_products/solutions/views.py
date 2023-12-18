from django.shortcuts import render
from txt_data_file import data
from .functions.f_simplex import *
from .functions.f_monte_karlo import *
import numpy as np
import matplotlib.pyplot as plt

def simplex_view(request):
    if 'btn_run_to_compute' in request.POST:
        res = simplex_found()
        x1 = res.x[0]
        x2 = res.x[1]
        num_of_products = len([x for x in res.x if x > 0])

        simplex_draw(x1,x2,'base_task')

        a_res_new = simplex_found_a()
        x1A = a_res_new.x[0]
        x2A = a_res_new.x[1]

        simplex_draw(x1A, x2A, 'a_task')

        b_res_new = simplex_found_b()
        x1B = b_res_new.x[0]
        x2B = b_res_new.x[1]

        simplex_draw(x1B, x2B, 'b_task')

        return render(request, 'solutions/simplex.html', {'x1': x1, 'x2': x2, 'revenue': num_of_products,
                                                          'x1A':x1A, 'x2A':x2A, 'a_res_new':-a_res_new.fun,
                                                          'x1B':x1B, 'x2B':x2B, 'b_res_new':-b_res_new.fun})
    else:
        return render(request, 'solutions/simplex.html')

def monte_karlo_view(request):
    if 'btn_run_to_compute' in request.POST:
        res = monte_carlo_found()
        x1 = res[0]
        x2 = res[1]

       # simplex_draw(x1,x2,'mk_base_task')

        # а) Заменим цены на 90% от исходных значений:
        a_res_new = monte_carlo_found_a()
        x1A = a_res_new[0]
        x2A = a_res_new[1]

        #simplex_draw(x1A, x2A, 'mk_a_task')

        # б) Увеличим суточный запас сырья на 10%:
        b_res_new = monte_carlo_found_b()
        x1B = b_res_new[0]
        x2B = b_res_new[1]

        #simplex_draw(x1B, x2B, 'mk_b_task')

        return render(request, 'solutions/monte_karlo.html', {'x1': x1, 'x2': x2,
                                                          'x1A':x1A, 'x2A':x2A, 'a_res_new':a_res_new,
                                                          'x1B':x1B, 'x2B':x2B, 'b_res_new':b_res_new})
    else:
        return render(request, 'solutions/monte_karlo.html')
