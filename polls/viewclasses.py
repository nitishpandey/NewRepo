from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.apps import apps
import requests
import json

class defaultView(View):
    def __init__(self):
        self.appconfig = app_config =  apps.get_app_config('polls')
        self.localdomain = app_config.localdomain
        self.azuredomain = app_config.proddomain
        self.upstoxapiendpoint = app_config.UPSTOX_API
        self.domainsarray = app_config.domainsarray
    
    def setcontext_(self,response,headers,url):
        import json
        context  = {'response_data': json.dumps(response.json()),
                'headers': json.dumps(headers),
                'domainsarray': self.domainsarray,
                'url':url
                }
        return context


    def get(self, request):
        """Handles GET requests to this view."""
        # Logic for processing GET requests (e.g., displaying a form)
        app_config = self.appconfig
        print(app_config.UPSTOX_API)
   
        code = request.GET.get("code")
        host = request.GET.get("state")
        #now use the code 
        
        if host == 'sandbox':
            targetdomain = app_config.localdomain
         
        else:
            targetdomain = app_config.proddomain
        
        your_client_id = getattr(app_config,host+'clientid') #2f21b28b-6251-4c8e-861f-6218bdf7e4b6'
        your_client_secret = getattr(app_config,host+'clientsecret') #'ojruk78aqh'
        your_redirect_url = targetdomain + f'polls'
        
        url = api_url = self.upstoxapiendpoint +'login/authorization/token'
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
        if response.status_code == 401:
            #return HttpResponse(response.json()['errors'][0]['message'] + "<br />Check the Auth Code Request Request")
            context = {'my_json_data': json.dumps(response.json())}
            return render(request, 'json_template.html', context)

        #context = {'message': 'This is a GET request'}
        # return render(request, 'my_template.html', context)
        context = self.setcontext_(response,headers,url)
         
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
        defaultview = defaultView()

        host = request.GET.get("state")
      
        url = defaultview.upstoxapiendpoint + 'user/get-funds-and-margin?segment=SEC'

        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {request.session["token"]}'
        }

        response = requests.get(url, headers=headers)
        print(request.session["token"])
        print(response.status_code)
        print(response.json()) 
        context = defaultview.setcontext_(response,headers,url)
        
      
        return render(request, 'json_template.html', context)

class optionsdata(View):
        def get(self, request):
            
            from datetime import datetime, timedelta

            current_month = datetime.now().month

            # Format the month with leading zero if necessary
            formatted_month = f"{current_month:02d}"
            current_day = date.today()
            options_data_not_found = True
            targetdate = current_day



            defaultview = defaultView()
            host = request.GET.get("state")
            url = defaultview.upstoxapiendpoint + f'option/chain?state={host}' 
            headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {request.session["token"]}'
            }
            counter = 0
            while options_data_not_found:
                params = {
                    'instrument_key': 'NSE_INDEX|Nifty 50',
                    'expiry_date': targetdate
                }

                response = requests.get(url, params=params, headers=headers)
                responsedata = response.json()
               # print(response)
                print(responsedata)
                counter += 1
                if responsedata['data']:
                    options_data_not_found = False
                if counter == 11:
                    options_data_not_found = False
                
                
                targetdate  = targetdate + timedelta(1)


            print(response.json())
            context = defaultview.setcontext_(response,headers,url)
         
      
            return render(request, 'json_template.html', context)
 