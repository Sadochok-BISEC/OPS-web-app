from django.urls import path
from . import views

urlpatterns = [
   path('simplex/', views.simplex_view, name='simplex'),
  # path('monte-karlo/', views.home, name='monte_karlo'),
]