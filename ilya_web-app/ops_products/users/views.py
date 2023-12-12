from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

data = {
    # In the form(on the right)
    'obj_message_titles':{
        'hello': 'Привет!',
        'hello_question': 'Привет! Здесь впервые?',
    },
    'obj_tab_titles':{
        # Generally
        # Auth
        'not_registered_page':'Добро пожаловать!',
        'login_page':'Авторизация',
        'signup_page':'Регистрация',

    }
}

# Create your views here.
def empty_home(request):
    return render(request, 'users/not_registered.html', data)

def login(request):
    return render(request, 'users/login.html', data)

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "users/signup.html"