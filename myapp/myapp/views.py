from django.http import HttpResponse
from django.shortcuts import render

import datetime

def home(request):
    isActive=False
    if request.method=='POST':
        check=request.POST.get("check")
        print(check)

        if check is not None:
            isActive=True

    
    #print("\n views.py request \n")
    #return HttpResponse("<h1> This is the home page <h1>")
    date=datetime.datetime.now()
    name="Yogesh DATA"
    list_of_fruits=[
        'banana',
        'apple',
        'guava',
        'banana',
        'pomegranate'
    ]
    student={
        'stu_name':"Yogesh",
        'stu_enroll':'201b318',
        'stu_college':"jaypee bguna"
    }
    
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_fruits':list_of_fruits,
        'student_data':student
    }

    return render(request,"home.html",data)

def aboutus(request):
    return render(request, "aboutus.html",{})
    #return HttpResponse("<h1> THIS IS ABOUTUS PAGE </H1>")

def services(request):
    return render(request,"services.html",{})