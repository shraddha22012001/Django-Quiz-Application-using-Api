from . import views
from django.urls import path,include
from quizapi import views as apiv  
urlpatterns = [
    path('jsonapi/',apiv.index),
    path('resultapi/',apiv.result),    
]
