from django.shortcuts import render

def Landing(requests):
    return render(requests,'index.html')

def Home(requests):
    return render(requests,'Home.html')

def Contact(requests):
    return render(requests,'Contact.html')

def Discuss(requests):
    return render(requests,'Discuss.html')

def Courses(requests):
    return render(requests,'Courses.html')