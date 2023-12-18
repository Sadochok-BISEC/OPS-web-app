from django.urls import path
from . import views

urlpatterns = [
   path('simplex/', views.simplex_view, name='simplex'),
   path('monte-karlo/', views.monte_karlo_view, name='monte_karlo'),
]