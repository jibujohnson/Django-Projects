from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

# Create your views here.

# @method_decorator(csrf_exempt,name='dispatch')
# class FactorialView(View):
#     def post(self,request):
#         request_body=request.body

@method_decorator(csrf_exempt,name='dispatch')
class SimpleInterestView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        p=form_data.get("principal")
        t=form_data.get("time")
        r=form_data.get("rate")
        si=(p * t * r)/100
        data={
                "Operation":"Simple Interest Calculator",
                "principal":p,
                "time":t,
                "rate":r,
                "simple interest":si
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class ProfitCalculatorView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        cp=form_data.get("cost_price")
        sp=form_data.get("selling_price")
        profit=sp-cp
        result={
            "Operation":"Profit Calculator",
            "Cost Price":cp,
            "Selling Price":sp,
            "Profit":profit
        }
        return JsonResponse(result)