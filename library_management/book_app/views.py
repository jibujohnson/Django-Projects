from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.

class GoodMorningView(View):
    def get(self,request):
        data={
            "Message":"Good Morning..!"
        }
        return JsonResponse(data)

class LibraryView(View):
    def get(self,request):
        result={
            "Library":"Central Library",
            "Location":"Idukki",
            "Status":"Open",
        }
        return JsonResponse(result)

class BookView(View):
    def get(self,request):
        data={
            "Book_Name":"Django for beginners",
            "Author":"Williams S. Vincent",
            "Price":650
        }
        return JsonResponse(data)

class StudentView(View):
    def get(self,request):
        result={
            "Name":"Jibu Johnson",
            "Course":"Python Django",
            "Batch":"June 2026",
            "Institution":"Luminar Technolab",
        }
        return JsonResponse(result)

class BookView(View):
    def get(self,request):
        data={
            "Books":[
                "python",
                "Django",
                "React",
                 "Java",
                "MySQL",
            ]
        }
        return JsonResponse(data)

class EmployeeView(View):
    def get(self,request):
        result={
            "ID":10,
            "Name":"Jithin Johnson",
            "Place":"Bahrain",
            "Designation":"Quality Checker",
            "Contact":7025193831,
            "Experience":"4 Years",
            "Qualification":"Higher Secondary",
        }
        return JsonResponse(result)