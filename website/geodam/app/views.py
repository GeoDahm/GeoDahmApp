from django.shortcuts import render

from .comparisonmodel import comparisonmodel

def output(request):
    if request.method == 'POST':
        image1= request.FILES['image1']
        image2= request.FILES['image2']
        output= comparisonmodel(image1,image2)

    return render(request,'output.html',context={'output':output})


def index(request):
    return render(request,'home1.html')

def imageupload(request):
    return render(request,'imageupload.html')
    
def riskzones(request):
    return render(request,'riskzones.html')

def Map4(request):
    return render(request,'Map4.html')

def riverflow(request):
    return render(request,'riverflow.html')
    
def about(request):
    return render(request,'about.html')
    