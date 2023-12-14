from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm
# Create your views here.

data = {
    # In the form(on the right)
    'obj_message_titles':{
        'hello': 'Привет!',
        'hello_question': 'Привет! Здесь впервые?',
        'about': 'О проекте',
        'contacts': 'Контакты',
    },
    'obj_contacts_info':{
        'txt_message':'Наше Веб-приложение, разработано по решению оптимизационных задач', # About.html call
        'author_name':'Автор: Ilya Bisec',
        'email':'Почта: ilya.borisov.bisec@gmail.com',
        'phone_number':'Телефон:(29)4911431 - Беларусь',
    },
    'obj_tab_titles':{
        # Generally
        'main_page':'Главная страница',
        'simplex_page':'Симплекс метод',
        'monte_page':'Монте-Карло метод',
        'about_page':'О проекте',
        'contacts_page':'Контакты',
        'exit_page':'Выйти',
        # Auth
        'not_registered_page': 'Добро пожаловать!',
        'login_page': 'Авторизация',
        'signup_page': 'Регистрация',
    }
}
@login_required
def home(request):
    return render(request, 'main/main.html', data)

def about(request):
    return render(request, 'main/about.html', data)

def contacts(request):
    return render(request, 'main/contacts.html', data)

# User authentication
def login_view(request):
    return render(request, 'main/login.html', data)

class SignUpView(CreateView):
    form_class = RegisterForm
    template_name = 'main/signup.html'
    success_url = '/ops_products/home'#reverse_lazy("main/main.html")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def signup_view(request):
    return render(request, 'main/signup.html', data)

def logout_view(request):
    return render(request, 'main/not_registered.html', data)