from django.urls import path
from . import views

urlpatterns = [
 path('', views.empty_home, name="empty_home"),
 path('sign-up', views.SignUp.as_view(), name="signup"),
 path('log-in', views.login, name="login"),
]