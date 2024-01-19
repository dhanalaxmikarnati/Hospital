from django.db import models

# Create your models here.
class Specialization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Doctor(models.Model):
    name = models.CharField(max_length=200)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    experience = models.IntegerField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    # Add more fields as needed

    def __str__(self):
        return self.name
    
class AvailableTimeSlot(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # Other fields to manage available time slots

    def __str__(self):
        return f"{self.doctor.name}'s available slot from {self.start_time} to {self.end_time}"