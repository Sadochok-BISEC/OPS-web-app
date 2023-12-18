from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm

from txt_data_file import data
# Create your views here.


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