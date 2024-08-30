from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,  'parameters_login_screen.html')  # Replace 'index.html' with your template's name


def doCheck():
    return 1

def session(request):
    c = doCheck() 
    request.session["0"] = 'dog'
    if request.session["0"]:
        print(f"printing {c} {request.session['0']}")
    return HttpResponse(request.session)
