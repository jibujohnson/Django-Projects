from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ExamApp.models import QuestionDb
from ExamApp.serializers import QuestionSerializer

# Create your views here.

class QuestionListCreateView(APIView):
    def get(self,request):
        qs=QuestionDb.objects.all().values()
        serializer_instance=QuestionSerializer(qs,many=True)
        return Response(data=serializer_instance.data)


