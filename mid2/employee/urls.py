from django.urls import path
from .views import Listemp,Delemp

urlpatterns=[
    path('Listemp', Listemp.as_view()),
    path('Delemp/<int:pk>/',Delemp.as_view())
]