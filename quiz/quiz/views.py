from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from quizapi.models import Exam

def home(request):
    return render(request,"home.html")

def quiz(request):
    questionlist = []
    questions = Exam.objects.all()  
    objcnt = Exam.objects.count()
    for ques in questions:
        questionlist.append({'question':ques.question,'option1':ques.option1,'option2':ques.option2,'option3':ques.option3,'option4':ques.option4,'correctans':ques.correctans})
    for i in range(objcnt):
        questionlist[i].update({'id':i})
    return render(request,"quiz.html",{'questions':questionlist}) 