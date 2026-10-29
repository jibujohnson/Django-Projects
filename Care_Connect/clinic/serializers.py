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

    def validate(self,validated_data):
        phone=validated_data.get("phone")
        appointment_date=validated_data.get("appointment_date")
        if Appointment.objects.filter(
            phone=phone,
            appointment_date=appointment_date).exists():
            raise serializers.ValidationError("Booking already exists.")
        else:
            return validated_data





