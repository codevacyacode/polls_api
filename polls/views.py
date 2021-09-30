from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Poll
from .serializers import PollSerializer

# Create your views here.

def index(request):
    return HttpResponse('Здесь будет список опросов.')

@api_view(['GET'])
def api_polls(request):
    if request.method == 'GET':
        thepolls = Poll.objects.all()
        serializer = PollSerializer(thepolls, many = True)
        return Response(serializer.data)