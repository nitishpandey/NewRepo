from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import requests
import json

class defaultView(View):
    def get(self, request):
        """Handles GET requests to this view."""
        # Logic for processing GET requests (e.g., displaying a form)

        code = request.GET.get("code")
        #now use the code 
        your_client_id = '2f21b28b-6251-4c8e-861f-6218bdf7e4b6'
        your_client_secret = 'ojruk78aqh'
        your_redirect_url = 'http://127.0.0.1:8000/polls'

        api_url = 'https://api.upstox.com/v2/login/authorization/token'
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
        response = requests.post(api_url, headers=headers, data=data)
        
        print(response.status_code)
        print(response.json())
        #context = {'message': 'This is a GET request'}
        # return render(request, 'my_template.html', context)
        context = {'my_json_data': json.dumps(response.json())}
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