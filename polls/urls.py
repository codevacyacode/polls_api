from django.urls import path, include
from .views import index, api_polls, api_questions, api_answers
from .views import api_whole_poll, api_active_polls, api_poll_answers
from .views import api_user

urlpatterns = [
    path('', index),
    path('api/polls/<int:pk>/answers/', api_poll_answers),
    path('api/polls/<int:pk>/', api_whole_poll),
    path('api/polls/active', api_active_polls),
    path('api/polls/', api_polls),
    path('api/questions/', api_questions),
    path('api/answers/<str:person>', api_user),
    path('api/answers/', api_answers),
]