from django.urls import path
from .views import Liststud,Delstud

urlpatterns=[
    path('Liststud', Liststud.as_view()),
    path('Delstud/<int:pk>/',Delstud.as_view())
]