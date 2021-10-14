from django.urls import path, include
from .views import index, api_polls

urlpatterns = [
	path('', index),
    path('api/polls/', api_polls),
    path('api/questions/', api_questions),
    path('api/answers/', api_answers),
]