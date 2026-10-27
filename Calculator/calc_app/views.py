from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class AdditionView(View):
    def post(self,request):
        request_body=request.body       # Type of request_body is JSON 
        # \r\n  "num1":15,\r\n      "num2":10\r\n
        # num1:15,num2:10
        form_data=loads(request_body)   # Converting JSON to Python Dictionary
        n1=form_data.get("num1")
        n2=form_data.get("num2")
        result=n1+n2
        print(request_body)
        data={
            "Sum":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class SubtractionView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get("num1")
        n2=form_data.get("num2")
        result=n1-n2
        data={
            "Difference":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class MultiplicationView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get("num1")
        n2=form_data.get("num2")
        result=n1*n2
        data={
            "Product":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class DivisionView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get("num1")
        n2=form_data.get("num2")
        result=n1/n2
        data={
            "Operation":"Division",
            "Division":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class ModulusView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get("num1")
        n2=form_data.get("num2")
        result=n1%n2
        data={
            "Operation":"Modulus",
            "Modulus":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class BMIView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        height=form_data.get("Height")
        weight=form_data.get("Weight")
        height_in_metre=height/100
        bmi=weight/(height_in_metre**2)
        data={
            "Operation":"BMI Calculator",
            "Height":height_in_metre,
            "Weight":weight,
            "BMI":bmi
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class AGEView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        birth_year=form_data.get("birth_year")
        current_year=form_data.get("current_year")
        age=current_year-birth_year
        data={
            "Operation":"AGE Calculator",
            "AGE":age
        }
        return JsonResponse(data)


@method_decorator(csrf_exempt,name='dispatch')
class PercentageView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        obt_marks=form_data.get("Obtained Marks")
        total_marks=form_data.get("Total Marks")
        percentage=(obt_marks/total_marks)*100
        data={
            "Operation":"Percentage Calculator",
            "Percentage":percentage
        }
        return JsonResponse(data)

