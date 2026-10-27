from rest_framework import serializers
from clinic.models import Doctor,Appointment

class Doctor_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields="__all__"
        # OR
        # fields=["id","doctor_name","specialization","...","..."]
        read_only_fields=["id"]
        
class Appointment_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields="__all__"
        read_only_fields=["id"]

