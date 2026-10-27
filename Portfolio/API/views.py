from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
# Create your views here.
class PortFolio(View):
    def get(self,request):
        data={
            "ID":10,
            "Full Name":"Jibu Johnson",
            "Professional Title":"Python Developer",
            "Bio":"An Enthusiastic learner",
            "DOB":"13/10/2005",
            "Email":"jibu008@gmail.com",
            "Contact":8714096478,
            "Location":"Ernakulam",
            "Github URL":"",
            "LinkedIn URL":"",
        }   
        return JsonResponse(data)

class Education(View):
    def get(self,request):
        result={
            "ID":20,
            "Institution":"Luminar Technolab",
            "Course":"Python Django Full Stack Development",
            "University":"InfoPark Kochi",
            "Location":"Kakkanad",
            "Start year":2026,
            "End year":2027,
            "Grade":"B",
            "Description":"Course ongoing",
        }
        return JsonResponse(result)

class ProjectView(View):
    def get(self,request):
        data=[
            {
                "ID":1,
                "Title":"Shawshank Redemption",
                "short_description":"A movie about jail escape",
                "technologies_used":["Python","Google"],
                "live_url":"https://movie/shawshank-redemption/",
                "github_url":"https://github/shawshank-redemption/",
                "image_url":"https://images/movie-images/",
                "Featured":True
            },
            {
                "ID":2,
                "Title":"Fight Club",
                "short_description":"A movie about starting a fight club",
                "technologies_used":["Python","Google"],
                "live_url":"https://movie/fight-club/",
                "github_url":"https://github/fight-club/",
                "image_url":"https://images/movie-images/",
                "Featured":True
            },
            {
                "ID":3,
                "Title":"Shutter Island",
                "short_description":"A movie about mysterious things happening in an Island",
                "technologies_used":["Python","Google"],
                "live_url":"https://movie/shutter-island/",
                "github_url":"https://github/shutter-island/",
                "image_url":"https://images/movie-images/",
                "Featured":True
            }
        ]
        return JsonResponse(data,safe=False)

class SkillView(View):
    def get(self,request):
        result=[
            {
                "id":101,
                "skill_name":"Python",
                "category":"Programming Language",
                "proficience":"Beginner",
                "years_of_experience":1
            },
            {
                "id":102,
                "skill_name":"MS Excel",
                "category":"Data Entry",
                "proficience":"Intermediate",
                "years_of_experience":2
            },
            {
                "id":103,
                "skill_name":"Libreoffice Writer",
                "category":"Documentation",
                "proficience":"Advanced",
                "years_of_experience":3
            }
        ]
        return JsonResponse(result,safe=False)

class ExperienceView(View):
    def get(self,request):
        data=[
            {
                "id":1,
                "job_title":"Software Engineer",
                "company_name":"techvyz",
                "location":"Kochi",
                "employment_type":"",
                "start_date":"10/12/2024",
                "end_date":"12/3/2025",
                "currently_working":"NO!",
                "description":"",
            },
            {
                 "id":2,
                "job_title":"QA Engineer",
                "company_name":"techwindz",
                "location":"Ernakulam",
                "employment_type":"",
                "start_date":"15/6/2025",
                "end_date":"5/1/2026",
                "currently_working":"NO!",
                "description":"",
            }
        ]
        return JsonResponse(data,safe=False)

class CertificateView(View):
    def get(self,request):
        result=[
            {
                "id":1,
                "certification_name":"Google Debugger",
                "issuing_organization":"Google",
                "issued_date":"14/7/2022"
            },
            {
                "id":2,
                "certification_name":"QA Engineering",
                "issuing_organization":"QA Techs",
                "issued_date":"22/5/2023"
            },
        ]
        return JsonResponse(result,safe=False)

class ServiceView(View):
    def get(self,request):
        data=[
            {
                "id":11,
                "service_name":"Python",
                "description":"Web developing using Python",
                "technologies_used":"PyCharm,VsCode "
            },
            {
                "id":12,
                "service_name":"Documentations",
                "description":"Making documentations like pdf,odt etc..",
                "technologies_used":"Libreoffice writer,MS Word",
            }
        ]
        return JsonResponse(data,safe=False)