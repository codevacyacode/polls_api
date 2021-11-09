from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Poll, Question, Answer
from .serializers import PollSerializer, QuestionSerializer, AnswerSerializer

# Create your views here.

def index(request):
    return HttpResponse('Здесь будет список опросов.')

@api_view(['GET'])
def api_polls(request):
    if request.method == 'GET':
        thepolls = Poll.objects.all()
        serializer = PollSerializer(thepolls, many = True)
        return Response(serializer.data)
        
@api_view(['GET'])
def api_questions(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many = True)
        return Response(serializer.data)
        
@api_view(['GET', 'POST'])
def api_answers(request):
    if request.method == 'GET':
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        str_choice = '; '.join(request.data['thechoice'])
        if not request.session.session_key:
            request.session.create()
        my_data = {
            'respondent': request.session.session_key,
            'question': request.data['thequestion'],
            'choice': str_choice
        }
        serializer = AnswerSerializer(data = my_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, 
            status = status.HTTP_400_BAD_REQUEST)
            
@api_view(['GET'])
def api_whole_poll(request, pk):
    # Получить все вопросы, указав id нужного опроса
    if request.method == 'GET':
        questions =  Question.objects.filter(poll = pk)
        serializer = QuestionSerializer(questions, many = True)
        return Response(serializer.data)
        