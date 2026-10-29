from django.shortcuts import render,get_object_or_404
from clinic.models import Doctor,Appointment
from clinic.serializers import Doctor_Serializer,Appointment_Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from datetime import time,timedelta,datetime

# Create your views here.

# VIEWS FOR DOCTOR

class DoctorListCreateView(APIView):
    def get(self,request):
        qs=Doctor.objects.all()
        serializer_instance=Doctor_Serializer(qs,many=True)
        return Response(data=serializer_instance.data)
    
    def post(self,request):
        form_data=request.data
        serializer_instance=Doctor_Serializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class DoctorRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):
        qs=get_object_or_404(Doctor,id=pk)
        serializer_instance=Doctor_Serializer(qs)
        return Response(data=serializer_instance.data)
    
    def put(self,request,pk):
        form_data=request.data
        doctor_object=get_object_or_404(Doctor,id=pk)
        serializer_instance=Doctor_Serializer(data=form_data,instance=doctor_object)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):
        doctor_object=get_object_or_404(Doctor,id=pk)
        doctor_object.delete()
        return Response(data={
        "Message":"ID Deleted."
        })

# VIEWS FOR APPOINTMENT

class AppointmentListCreateView(APIView):
    def get(self,request):
        qs=Appointment.objects.all()
        serializer_instance=Appointment_Serializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=Appointment_Serializer(data=form_data)
        if serializer_instance.is_valid():
            print(serializer_instance.validated_data)
            # actual_data=serializer_instance.validated_data
            appointment_date=serializer_instance.validated_data.get("appointment_date")
            doctor_id=serializer_instance.validated_data.get("doctor_id")
            last_appointment=Appointment.objects.filter(appointment_date=appointment_date,doctor_id=doctor_id).order_by("-token_number").first()
            if last_appointment is None:
                form_data["token_number"]=1
                form_data["appointment_time"]=time(10,0)
            else:
                form_data["token_number"]=last_appointment.token_number+1
                current_time=datetime.combine(appointment_date,last_appointment.appointment_time)
                next_time=current_time+timedelta(minutes=15)
                
                # Adding lunch brake time
                if next_time.time()==time(13,0):
                    next_time=datetime.combine(appointment_date,time(14,0))

                # Moving to the next day after 6 PM
                if next_time.time()>=time(18,0):
                    raise serializers.ValidationError("No slots available for today.")
                    

                form_data["appointment_time"]=next_time


            qs=Appointment.objects.create(**form_data)
            serializer_instance=Appointment_Serializer(qs)
            return Response(data={
                "Message":"Appointment Booked Successfully.",
                "Your Token Number is":form_data["token_number"],
                "Your Appointment Time is":form_data["appointment_time"]
            })
        else:
            return Response(data=serializer_instance.errors)











