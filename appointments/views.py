from django.shortcuts import render, redirect
from django.contrib import messages
from doctors.models import Doctor, AvailableTimeSlot
from patients.admin import PatientAdmin
from patients.models import Patient 
from .models import Appointment
from datetime import datetime 

def generate_patients(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        problems = request.POST.get('problems')
        
        Patient.objects.create(
            name=name,
            age=age,
            email=email,
            contact_number=contact_number,
            problems=problems
        )
        return redirect('appointments')  # Redirect after creating the patient

def appointments(request):
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor')
        appointment_time = request.POST.get('appointment_time')
        patient_name = request.POST.get('patient_name')
        
        try:
            doctor = Doctor.objects.get(id=doctor_id)
        except Doctor.DoesNotExist:
            messages.error(request, 'Doctor not found. Please select a valid doctor.')
            return redirect('appointments')
        
        # Generate patient upon appointment booking
        generate_patients(request)
        
        # Retrieve or create a patient based on name
        # 
        # patient, created = Patient.objects.get_or_create(name= id)
        
        appointment_datetime = datetime.strptime(appointment_time,'%Y-%m-%dT%H:%M')

        available_slot = AvailableTimeSlot.objects.filter(
            doctor=doctor,
            start_time__lte=appointment_datetime,
            end_time__gte=appointment_datetime
        ).exists()

        if available_slot:
            appointment = Appointment.objects.create(
                doctor=doctor,
                appointment_time=appointment_datetime,
                patient= PatientAdmin,
            )
            messages.success(request, 'Appointment booked successfully!')
        else:
            messages.error(request, 'Selected time slot is not available.')

        return redirect('appointments')
    
    doctors = Doctor.objects.all()
    appointments = Appointment.objects.all()
    context = {
        'doctors': doctors,
        'appointments': appointments,
    }
    return render(request, 'appointments.html', context)
