from django.shortcuts import render

# Create your views here.
def simplex_view(request):
    return render(request, 'solutions/simplex.html')