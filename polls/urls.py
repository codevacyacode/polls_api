from django.urls import path, include
from .views import api_polls

urlpatterns = [
	path('api/polls/', api_polls),
    path('poll', include('polls')),
]