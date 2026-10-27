from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class MyClass(APIView):
    def get(self,request):
        return Response({"msg":"HELLO...!"})

class AdditionView(APIView):
    def post(self,request):
        x=request.data.get("num1")
        y=request.data.get("num2")
        result=x+y
        return Response({
            "First number":x,
            "Second number":y,
            "Result":result
        })

class SubtractionView(APIView):
    def post(self,request):
        x=request.data.get("num1")
        y=request.data.get("num2")
        result=x-y
        return Response({
            "First number":x,
            "Second number":y,
            "Result":result
        })

class MultiplicationView(APIView):
    def post(self,request):
        x=request.data.get("num1")
        y=request.data.get("num2")
        result=x*y
        return Response({
            "First number":x,
            "Second number":y,
            "Result":result
        })

class LargestView(APIView):
    def post(self,request):
        x=request.data.get("num1")
        y=request.data.get("num2")
        if x>y:
            result=x
        else:
            result=y
        return Response({
            "First number":x,
            "Second number":y,
            "Largest":result
        })

class FahrenheitView(APIView):
    def post(self,request):
        celsius=request.data.get("celsius")
        fahrenheit=(celsius*9/5)+32
        return Response({"Fahrenheit":fahrenheit})
