from datetime import date
from django.http.response import JsonResponse
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
        response = request.post(api_url, headers=headers, data=data)
        
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
        name = requests.POST.get('name')
        return HttpResponse(f'Hello, {name}! Your form was submitted successfully.')

  

#view that renders a template that shows the JSON as a table
class userProfile(View):
    def get(self,request):
        jsondata = request.session['userProfile']
        context = {'my_json_data': json.dumps(jsondata)}
        return render(request, 'json_template.html', context)

class predictor(View):
    def get(self, request): 
        defaultview = defaultView()
        datafetcher = datafetch()
        #use get method of the datafetch class and then convert the JsonResponse object contents to string and then to json

        options_chain = json.loads(datafetcher.get(request,'options_chain').content.decode('utf-8'))
       # print("This:" + json.dumps(options_chain))
       # data = json.load(options_chain)
        data = options_chain['data'] #[1]
        #print("This:" + json.dumps(data))
       
        keys_to_keep = ["strike_price"]
        #for members in data:
        filtered_data = ''
        for items in data:
                filtered_data = {k: v for k, v in items.items() if k in keys_to_keep}

        return JsonResponse(filtered_data)
        context = defaultview.setcontext_(filtered_data,headers,url)
       
        return render(request, 'json_template.html', context)

class datafetch(View):
    def get(self, request,path_pattern): #3 arguments because we are using re_path
        defaultview = defaultView()
       # host = request.GET.get("state")
      
       #some new syntax for switch. No fall through to next case.
        match path_pattern:
            case 'trades':
                url = defaultview.upstoxapiendpoint + 'portfolio/short-term-positions'
            case 'funds':
                url = defaultview.upstoxapiendpoint + 'user/get-funds-and-margin?segment=SEC'
            case _ :
                url = defaultview.upstoxapiendpoint + 'option/chain?'
            
        #request.session['auth_code']
        #print("Printing session key before making call to see funds:")
        #print(request.session.session_key)
       
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {request.session["auth_code"]}'
        }
        #print(url)
        if(path_pattern == 'options_chain'):
            response = self.options_chain(request,headers,url)
        else:
            response = requests.get(url, headers=headers)
        
        accept_header = request.META.get('HTTP_ACCEPT')
        
        if 'application/json' in accept_header:
            return JsonResponse(response.json())
        context = defaultview.setcontext_(response,headers,url)
        
        return render(request, 'json_template.html', context)

     
    
        
    
    def options_chain(self,request,headers,url):
            from datetime import datetime, timedelta

            current_month = datetime.now().month

            # Format the month with leading zero if necessary
            formatted_month = f"{current_month:02d}"
            current_day = date.today()
            options_data_not_found = True
            targetdate = current_day
            counter = 0
            if request.GET.get('index') == 'BN':
                instrument = 'NSE_INDEX|Nifty Bank'
            else:
                instrument = 'NSE_INDEX|Nifty 50'

            while options_data_not_found:
                params = {
                    'instrument_key': instrument ,
                    'expiry_date': targetdate
                }

                response = requests.get(url, params=params, headers=headers)
                responsedata = response.json()
               # print(response)
               # print(responsedata)
                counter += 1
                if responsedata['data']:
                    options_data_not_found = False
                if counter == 11: #max days to try
                    options_data_not_found = False
                
                
                targetdate  = targetdate + timedelta(1)
            print(response)
            return response

           
            context = defaultview.setcontext_(response,headers,url)
         
      
            return render(request, 'json_template.html', context)

