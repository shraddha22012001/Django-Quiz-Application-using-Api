from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Exam
import json

def index(request):
    q = Exam.objects.all()
    data = serialize('json',q,fields={'id','correctans'})
    return HttpResponse(data,content_type="application/json")

def result(request):
    print("req received")
    userans=request.GET['userans']
    corrans=request.GET['corrans']
    useranslist=json.loads(userans)
    corranslist=json.loads(corrans)
    score=0
    for i in range(len(useranslist)):
        if useranslist[i]==corranslist[i]:
            score+=1   
    resultdict={'score':score,'percentage':score/(len(corranslist))*100}
    json_response=json.dumps(resultdict,indent=5)
    print("json response",json_response)
    return HttpResponse(json_response,content_type='application/json')   

