from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from hackaway.scrapper import *
import requests
def index(request):
    return render(request,'hackaway/index.html')

def sanitize(request):
    url=request.POST['url']
    value=request.POST.get('radio',False)
    if value=="low":
        res=safesite(url,"low")
    elif value=="med":
        res=safesite(url,"med")
    elif value=="high":
        res=safesite(url,"high")

    score=seccheck(url)
    res='<script>alert("The security score is:'+str(score)+'.")</script>' + res
    return HttpResponse(res)
    # scrape and sanitize the output
    # send the result to another HTML page

def seccheck(url):
    baseurl="https://api.threatintelligenceplatform.com/v1/malwareCheck?domainName=threatintelligenceplatform.com&apiKey=at_FdlCgOLdAmhuP67o2x88QaE4mqLvc&domainName="
    url=baseurl+url
    res=requests.get(url)
    res=res.json()
    return res['safeScore']


def safecheckwebsite(request):
    url=request.POST['url']
    score=seccheck(url)
    res='<script>alert("The security score is:'+str(score)+'.")</script>' + res
    return HttpResponse(res)
