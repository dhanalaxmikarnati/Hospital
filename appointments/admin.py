from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_time',)
    list_filter = ('patient','doctor','appointment_time')
    search_fields = ('patient', 'doctor','appointment_time')
    # Add more configurations as needed
    
    