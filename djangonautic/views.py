from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    # return HttpResponse("This is the about page")
    return render(request, "about.html")

def home(request):
    # return HttpResponse("This is the HOME page")
     return render(request, "index.html")