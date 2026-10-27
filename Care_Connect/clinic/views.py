from django.shortcuts import render,get_object_or_404
from clinic.models import Doctor,Appointment
from clinic.serializers import Doctor_Serializer,Appointment_Serializer
from rest_framework.views import APIView
from rest_framework.response import Response

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

