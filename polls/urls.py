from django.urls import path, include
from .views import index, api_polls, api_questions, api_answers, api_whole_poll

urlpatterns = [
    path('', index),
    path('api/polls/<int:pk>/', api_whole_poll),
    path('api/polls/', api_polls),
    path('api/questions/', api_questions),
    path('api/answers/', api_answers),
]