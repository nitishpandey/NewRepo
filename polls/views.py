from django.shortcuts import render
import requests
import json
# Create your views here.

from django.http import HttpResponse

def index(request):
    code = request.GET.get("code")

    #now use the code 
    your_client_id = '2f21b28b-6251-4c8e-861f-6218bdf7e4b6'
    your_client_secret = 'ojruk78aqh'
    your_redirect_url = 'http://127.0.0.1:8000/polls'

   
    if 'auth_code' in request.session:
        # The key exists in the session
        your_access_token = request.session['auth_code']
        url = 'https://api.upstox.com/v2/user/profile'
        headers = {
                    'Accept': 'application/json',
                    'Authorization': f'Bearer {your_access_token}'
                }
        print(headers)
        response = requests.get(url, headers=headers)

    else:
    # The key does not exist in the session
    # ... handle the case where the key is missing
    
        url = 'https://api.upstox.com/v2/login/authorization/token'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
                }

        data = {
                    'code': f'{code}',
                    'client_id': f'{your_client_id}',
                    'client_secret': f'{your_client_secret}',
                    'redirect_uri': f'{your_redirect_url}',
                    'grant_type': 'authorization_code',
                }
        print(data)
        response = requests.post(url, headers=headers, data=data)
        
        #request.session['auth_code'] = response.json()['access_token'] 
    
    print(response.status_code)
    print(response.json())
    
    return HttpResponse(f"The code is {code}")
