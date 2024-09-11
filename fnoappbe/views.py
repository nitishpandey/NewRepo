from types import NotImplementedType
from django.shortcuts import render

from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
from django.http import HttpResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt 

def index(request):
    return render(request,  'index.html')  

#called from FE form with email id or upstox client id and secret. 
#These are then stored in the session. They are used once we get the access token 
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))  # Decode and parse JSON
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)  # Handle invalid JSON

        client_id = data.get('email')
        secret = data.get('email')
        request.session['client_id'] = client_id
        request.session['secret'] = secret
        print(client_id);
    #else return error code in response so that the user is not taken to upstox login
    return render(request, 'index.html')

def emptyjson(request):
   return JsonResponse({'articles':[{'title':'first news'}]});

def NotImplementedType(request):
   return JsonResponse({'error':[{'message':'first build it'}]}); 

@csrf_exempt  # Exempt this view from CSRF protection
def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})