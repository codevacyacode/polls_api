from rest_framework import serializers
from .models import Poll, Question, Answer

class PollSerializer(serializers.ModelSerializer):
	class Meta:
		model = Poll
		fields = ('id', 'title', 'date_a', 'date_b', 'description')
        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'poll', 'title', 'type', 'option0', 'option1', 'option2', 'option3')
        
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'respondent', 'question', 'choice')