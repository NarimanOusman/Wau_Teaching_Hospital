from django.shortcuts import render

# Crdeate your views here.
def index(request):
    return render(request, 'index.html')