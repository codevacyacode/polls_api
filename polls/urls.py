from django.urls import path
from .views import api_polls

urlpatterns = [
	path('api/polls/', api_polls),
]