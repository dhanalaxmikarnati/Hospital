from django.contrib import admin
from .models import Doctor,Specialization,AvailableTimeSlot

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'experience', 'contact_number', 'email')
    list_filter = ('specialization',)
    search_fields = ('name', 'email')
    # Add more configurations as needed
@admin.register(AvailableTimeSlot)
class AvailableTimeSlotAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'start_time', 'end_time')
   