from django.shortcuts import render
import requests
import json
from django.apps import apps

from django.core.exceptions import ValidationError
# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse

def getAuthCode(request):
    
            code = request.GET.get("code")
            mode = request.GET.get("state")
            app_config =  apps.get_app_config('polls')
            domainsarray = app_config.domainsarray
            upstoxapiendpoint = app_config.UPSTOX_API
                
            #now use the code 
            your_client_id = domainsarray[mode]['clientid'] #'2f21b28b-6251-4c8e-861f-6218bdf7e4b6'
            your_client_secret = domainsarray[mode]['clientsecret'] #'ojruk78aqh'
            your_redirect_url = domainsarray[mode]['url']+'/authcode'   # 'http://127.0.0.1:8000/authcode'
            
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
            print(url) # headers)
            try:
                response = requests.post(url, headers=headers, data=data)
                if response.status_code == 200:
                    rdata = response.json()
                    print(rdata)
                    if rdata['broker'] == 'UPSTOX':
                        request.session['auth_code'] = rdata['access_token'] 
                    else:
                        raise ValidationError("Invalid response. Please try again.")

                else:
                    print(response)
                   # raise ValidationError("Invalid data in response. Please check your input.")
                  
            except requests.exceptions.RequestException as e:
                print(f"Error during request: {e}")
       
            return response.status_code
            print(response.json())
    

def index(request):
    app_config =  apps.get_app_config('polls')
    fedomain = app_config.fedomain
            
    if 'auth_code' in request.session:
        # The key exists in the session but is it valid? lets check 

        your_access_token = request.session['auth_code']
        url = 'https://api.upstox.com/v2/user/profile'
        headers = {
                    'Accept': 'application/json',
                    'Authorization': f'Bearer {your_access_token}'
                }
        print(headers)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
          status = 201 # baseically do nothing
        else:
          status =  getAuthCode(request)


    else:
    # The key does not exist in the session
    # ... handle the case where the key is missing
        status = getAuthCode(request)
    
    if(status == 200 or status == 201):
        response = {'response': status, 'message': 'The code is '+ request.session['auth_code'] + 'and ' + request.session.session_key}
        return_url = '/trades'
        responsevar = JsonResponse(response)  
    else:
       me = {'message':"An error. Your submit to the app login is stale."}
       responsevar = JsonResponse(me)
       return_url = '/login?error='+me
    new_url = fedomain + return_url  # Replace with your desired URL

    print("printing below:")
    print(response)
    print(request.session['auth_code'])
    print("printed above")

   
    javascript_code = f"""
    <script>
        window.location.href = '{new_url}';
    </script>
    """

    # Create the HttpResponse with the JavaScript content
    response = HttpResponse(javascript_code, content_type='text/html')

    return response
 