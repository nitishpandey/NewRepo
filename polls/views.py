from django.shortcuts import render
import requests
import json
# Create your views here.

from django.http import HttpResponse

def index(request):
    code = request.GET.get("code")
    mode = request.GET.get("state")
    #now use the code 
    if mode == 'sandbox':
        your_client_id = '2f21b28b-6251-4c8e-861f-6218bdf7e4b6'
        your_client_secret = 'ojruk78aqh'
        your_redirect_url = 'http://127.0.0.1:8000/polls'
    else:
        your_client_id = 'cc982509-6fa9-4046-939d-41b190aa9252'
        your_client_secret = ''
        your_redirect_url = 'https://upstox-app.azurewebsites.net/polls'
   
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
        try:
            response = requests.post(url, headers=headers, data=data)
            if response.status_code == 200:
               rdata = response.json()
               print(rdata)
               if rdata['status'] == 'success':
                    request.session['auth_code'] = rdata['access_token'] 
               else:
                    raise ValidationError("Invalid response. Please try again.")

            else:
               raise ValidationError("Invalid data. Please check your input.")

        except requests.exceptions.RequestException as e:
            print(f"Error during request: {e}")
       
    print(response.status_code)
    print(response.json())
    
    return HttpResponse(f"The code is {code}, {request.session['auth_code']} and {request.session['client_id']}")
