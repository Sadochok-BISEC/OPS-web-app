from django.shortcuts import render
# Create your views here.

def show_test(request):
    return render(request, 'main/main.html')

def about(request):
    return render(request, 'main/about.html')