from django.shortcuts import render

def Landing(requests):
    return render(requests,'index.html')