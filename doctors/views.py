from django.shortcuts import render
from .models import Doctor

def doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors})


def hospital(request):
    return render(request,'hospital.html')