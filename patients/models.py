from django.db import models
import uuid
# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    problems = models.TextField()
    assigned_doctor = models.ForeignKey('doctors.Doctor', on_delete=models.SET_NULL, null=True, blank=True)
    unique_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    # Add more fields as needed
    
    def __str__(self):
        return self.name