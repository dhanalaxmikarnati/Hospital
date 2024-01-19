from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'contact_number','problems')
    search_fields = ('name', 'email', 'contact_number')
    # Add more configurations as needed