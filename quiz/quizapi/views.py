from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Exam
import json

def index(request):
    q = Exam.objects.all()
    data = serialize('json',q,fields={'id','question','option1','option2','option3','option4','correctans'},indent=5)
    return HttpResponse(data,content_type="application/json")

def result(request):
    userans=request.GET['userans']
    corrans=request.GET['corrans']
    userlist=json.loads(userans)
    corlist=json.loads(corrans)
    score=0
    for i in range(len(userlist)):
        if userlist[i]==corlist[i]:
            score+=1   
    resultdict={'score':score,'per':score/(len(corlist))*100}
    json_response=json.dumps(resultdict,indent=5)
    return HttpResponse(json_response,content_type='application/json')   

