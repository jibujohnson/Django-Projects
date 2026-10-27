from rest_framework import serializers
from Repository.models import QuestionDb

class QuestionSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=100)
    language=serializers.ChoiceField(choices=QuestionDb.Language_Choices)
    difficulty_level=serializers.ChoiceField(choices=QuestionDb.Difficulty_Choices)
    topic=serializers.CharField(max_length=100)
    score=serializers.IntegerField()
    published_date=serializers.DateTimeField(read_only=True)
    notes=serializers.CharField()
    sample_input=serializers.CharField(max_length=500)
    sample_output=serializers.CharField(max_length=500)
    is_active=serializers.BooleanField(default=True)

class SubmissionSerializer(serializers.Serializer):
    answer=serializers.CharField()
    question_id=serializers.IntegerField()
    points=serializers.IntegerField(read_only=True)
    owner=serializers.CharField()
    remarks=serializers.CharField(read_only=True)
    submission_date=serializers.DateTimeField(read_only=True)
    

    def validate(self,validated_data):
        question_id=validated_data.get("question_id")
        if not QuestionDb.objects.filter(id=question_id).exists():
            raise serializers.ValidationError("Question doesn't exists!")
        return validated_data




    


