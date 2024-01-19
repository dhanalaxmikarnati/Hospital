# from django.http import HttpResponse
# from patients.models import Patient

# def generate_patients(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         age = request.POST.get('age')
#         email = request.POST.get('email')
#         contact_number = request.POST.get('contact_number')
#         problems = request.POST.get('problems')
        
#         Patient.objects.create(
#             name=name,
#             age=age,
#             email=email,
#             contact_number=contact_number,
#             problems=problems
#         )
#         return HttpResponse("Patient created successfully!")  # Send a response after creating the patient
    
    
from patients.models import Patient
import random
import string

def generate_patients(num_patients=10):
    for i in range(num_patients):
        name = f"Patient-{i+1}"
        age = random.randint(18, 60)
        email = f"patient{i+1}@example.com"
        contact_number = ''.join(random.choices(string.digits, k=10))
        problems = "Some problems description..."
        
        Patient.objects.create(
            name=name,
            age=age,
            email=email,
            contact_number=contact_number,
            problems=problems
        )

