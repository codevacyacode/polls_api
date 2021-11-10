from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Poll, Question, Answer
from .serializers import PollSerializer, QuestionSerializer, AnswerSerializer
from datetime import date

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
def api_active_polls(request):
    if request.method == 'GET':
        thepolls = Poll.objects.filter(date_a__lte = datetime.date.today(), 
        date_b__gt = datetime.date.today())
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

@api_view(['GET'])
def api_poll_answers(request, pk):
    # Получить все ответы по номеру опроса
    if request.method == 'GET':
        our_questions = [] # Список id вопросов нужного опроса
        for question in Question.objects.filter(poll = pk):
            our_questions.append(question.id)
        answers = []
        for oq in our_questions:
            for a in Answer.objects.filter(question = oq):
                answers.append(a)
        serializer = AnswerSerializer(answers, many = True)
        return Response(serializer.data)


@api_view(['GET'])
def api_user(request, person):
    # Получить все ответы пользователя
    if request.method == 'GET':
        answers = Answer.objects.filter(respondent = person)
        serializer = AnswerSerializer(answers, many = True)
        return Response(serializer.data)
