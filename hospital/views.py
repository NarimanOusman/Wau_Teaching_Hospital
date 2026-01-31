from django.shortcuts import render

# Crdeate your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def appointment(request):
    return render(request, 'appointment.html')

def services(request):
    return render(request, 'services.html')

def doctors(request):
    return render(request, 'doctors.html')

def accident_report(request):
    return render(request, 'accident_report.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')