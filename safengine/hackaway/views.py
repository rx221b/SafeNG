from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from hackaway.scrapper import *

def index(request):
    return render(request,'hackaway/index.html')

def sanitize(request):
    url=request.POST['url']
    res=safesite(url)
    return HttpResponse(res)
    # scrape and sanitize the output
    # send the result to another HTML page


