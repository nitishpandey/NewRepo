from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.apps import apps
import requests
import json

class defaultView(View):
    def get(self, request):
        """Handles GET requests to this view."""
        # Logic for processing GET requests (e.g., displaying a form)
        my_app_config = apps.get_app_config('polls')
        localdomain = my_app_config.localdomain
        azuredomain = my_app_config.azuredomain
        print(my_app_config.UPSTOX_API)

        code = request.GET.get("code")
        #now use the code 
        your_client_id = '2f21b28b-6251-4c8e-861f-6218bdf7e4b6'
        your_client_secret = 'ojruk78aqh'
        your_redirect_url = localdomain + 'polls'
        
        api_url = my_app_config.UPSTOX_API +'login/authorization/token'
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
        print(api_url)
        response = requests.post(api_url, headers=headers, data=data)
        
        print(response.status_code)
        print(response.json())
        #context = {'message': 'This is a GET request'}
        # return render(request, 'my_template.html', context)
        context = {'my_json_data': json.dumps(response.json()),
                   'localdomain': localdomain,
                   'azuredomain': azuredomain}
        a = request.session['token'] = response.json()['access_token']   
        print( a)
        return render(request, 'json_template.html', context)
 
    
    def post(self, request):
        """Handles POST requests to this view."""
        # Logic for processing POST requests (e.g., handling form submissions)
        name = request.POST.get('name')
        return HttpResponse(f'Hello, {name}! Your form was submitted successfully.')

#view that renders a template that shows the JSON as a table
class userProfile(View):
    def get(self,request):
        jsondata = request.session['userProfile']

        
        context = {'my_json_data': json.dumps(jsondata)}
        return render(request, 'json_template.html', context)

class funds(View):
    def get(self, request):
        my_app_config = apps.get_app_config('polls')
        url = my_app_config.UPSTOX_API +'user/get-funds-and-margin?segment=SEC'

        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {request.session["token"]}'
        }

        response = requests.get(url, headers=headers)
        print(request.session["token"])
        print(response.status_code)
        print(response.json())
        context = {'my_json_data': json.dumps(response.json()),
                   'headers': json.dumps(headers),
                   'localdomain': 'http://127.0.0.1:8000/',
                   'url':url,
                   'azuredomain': 'https://upstox-app.azurewebsites.net/'}
      
        return render(request, 'json_template.html', context)

class optionsdata(View):
        def get(self, request):
            
            my_app_config = apps.get_app_config('polls')
            url = my_app_config.UPSTOX_API + 'option/chain'
            params = {
                'instrument_key': 'NSE_INDEX|Nifty 50',
                'expiry_date': '2024-08-29'
            }
            headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {request.session["token"]}'
            }

            response = requests.get(url, params=params, headers=headers)

            print(response.json())
            context = {'my_json_data': json.dumps(response.json()),
                   'headers': json.dumps(headers),
                   'localdomain': 'http://127.0.0.1:8000/',
                   'url':url,
                   'azuredomain': 'https://upstox-app.azurewebsites.net/'}
      
            return render(request, 'json_template.html', context)
 