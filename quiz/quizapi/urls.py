
from django.urls import path,include
from quizapi import views  
urlpatterns = [
    path('jsonapi/',views.index),
    path('resultapi/',views.result),    
]
