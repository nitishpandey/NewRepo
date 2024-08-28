from django.shortcuts import render

def index(request):
    return render(request,  'parameters_login_screen.html')  # Replace 'index.html' with your template's name
