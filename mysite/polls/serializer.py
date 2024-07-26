from rest_framework import serializers
from .models import Choice, Question

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['question', 'choice_text', 'votes']

class QuestionSerializer(serializers.ModelSerializer):
    choice = ChoiceSerializer(many=True)
    
    class Meta:
        model = Question
        fields = []