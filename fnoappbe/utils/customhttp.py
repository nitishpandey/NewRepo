import requests
from ..views import logout
import json
from django.http.response import JsonResponse



#returns json of the response
def make_get_call(request,url,params={}, header={}):
    try:
        
        response = requests.get(url,params=params,headers=header)
        # Check the status code
        response.raise_for_status()  # Raises an HTTPError for bad status codes (4xx and 5xx)

        # Process the response (assuming it's JSON)
        return JsonResponse(response.json())
        
    except requests.exceptions.HTTPError as e:
        # Handle HTTP errors (4xx and 5xx status codes)
        logout(request)
        return JsonResponse({'status':'error','message': 'No Longer Logged In','url':'/login'},status=response.status)
        
    except json.JSONDecodeError as e:
                     # Handle invalid JSON responses
        return JsonResponse({'status':'error','message':"error in decoding the json"},status=500)
    except  requests.exceptions.RequestException as e:
            # Handle network errors (connection errors, timeouts, etc.)
            return JsonResponse({'status':'error','message':"error in connection."},status=500)
    except:
            return JsonResponse({'status':'error','message':"unknown error."},status=500)
        
    