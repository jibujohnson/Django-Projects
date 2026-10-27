from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.
class GoodMorningView(View):
    def get(self,request):
        data={
            "message":"HEY, Good Morning!"
        }
        # Python native type
        # Dictionary --> JSON

        return JsonResponse(data)

class HelloWorldView(View):
    def get(self,request):
        result={
            "Hello":"Introduction to django",
            "Message":"Hello World!"
        }
        return JsonResponse(result)

class GoodAfternoonView(View):
    def get(self,request):
        result={
            "Time":"HI Jibu, Good Afternoon!"
        }
        return JsonResponse(result)

class GoodNightView(View):
    def get(self,request):
        result={
            "Now":"BYE Jibu, Good Night!"
        }
        return JsonResponse(result)