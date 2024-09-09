from django.shortcuts import render

from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from django.http import HttpResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt 

def index(request):
   return render(request,  'index.html')  

def emptyjson(request):
   return JsonResponse({'articles':[{'title':'first news'}]});
    
@csrf_exempt  # Exempt this view from CSRF protection
def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})