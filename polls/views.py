from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Poll
from .serializers import PollSerializer

# Create your views here.

@api_view(['GET'])
def api_polls(request):
    if request.method == 'GET':
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many = True)
        return Response(serializer.data)