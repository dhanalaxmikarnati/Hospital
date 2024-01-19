from django.shortcuts import render
from .models import Patient

# Create your views here.
def patients(request):
    patients = Patient.objects.all()
    return render(request, 'patients.html', {'patients': patients})