from django.urls import path
from .views import Listtech,Deltech

urlpatterns=[
    path('Listtech', Listtech.as_view()),
    path('Deltech/<int:pk>/',Deltech.as_view())
]