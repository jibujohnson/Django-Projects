from django.db import models

# Create your models here.

class Doctor(models.Model):
    doctor_name=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100)
    experience=models.PositiveIntegerField()
    hospital=models.CharField(max_length=100)
    consulting_fee=models.PositiveIntegerField()
    availability=models.BooleanField(default=True)

    def __str__(self):
        return self.doctor_name

class Appointment(models.Model):
    patient_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    doctor_id=models.IntegerField()
    appointment_date=models.DateField()
    appointment_time=models.TimeField(null=True,blank=True)
    token_number=models.PositiveIntegerField(editable=False,null=True)
    problem=models.TextField()
    status=models.CharField(max_length=200,default="Pending")
    prescription=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name