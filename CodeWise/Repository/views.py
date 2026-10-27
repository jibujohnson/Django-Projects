from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from Repository.models import QuestionDb,SubmissionDb
from Repository.serializers import QuestionSerializer,SubmissionSerializer

# Create your views here.

class QuestionListCreateView(APIView):
    def get(self,request):
        # Retrieve all questions from the QuestionDb model
        qs=QuestionDb.objects.all().values()

        serializer_instance=QuestionSerializer(qs,many=True)    # Serialize the queryset

        # result=list(qs)     # Converts the queryset to a list of dictionaries

        return Response(data=serializer_instance.data)  # Return the serialized data as a response 

    # POST method for adding questions
    def post(self,request):

        form_data=request.data      # Get the form data from the request

        serializer_instance=QuestionSerializer(data=form_data)

        if serializer_instance.is_valid():
            original_data=serializer_instance.validated_data

            # Create a new question instance using the form data
            QuestionDb.objects.create(**form_data)

            return Response({"Message":"Question added successfully!"})
        
        else:
            return Response(data=serializer_instance.errors)
            
class QuestionRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):

        qs=QuestionDb.objects.get(id=pk)

        serializer_instance=QuestionSerializer(qs)

        return Response(data=serializer_instance.data)

    def put(self,request,pk):
        form_data=request.data      # Get the data from client
        serializer_instance=QuestionSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            QuestionDb.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):
        QuestionDb.objects.filter(id=pk).delete()
        return Response({
            "Message":"Question deleted successfully!"
        })


class SubmissionListCreateView(APIView):
    def get(self,request):
        qs=SubmissionDb.objects.all()
        serializer_instance=SubmissionSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=SubmissionSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            SubmissionDb.objects.create(**actual_data)
        return Response(data=serializer_instance.data)

class SubmissionRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):
        # qs=SubmissionDb.objects.get(id=pk)
        qs=get_object_or_404(SubmissionDb,id=pk)
        serializer_instance=SubmissionSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self,request):
        pass

class EvaluateSubmissionView(APIView):
    def put(self,request,pk):
        form_data=request.data
        SubmissionDb.objects.filter(id=pk).update(**form_data)
        return Response(data={
            "Message":"Updated!"
        })