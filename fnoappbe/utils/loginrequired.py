from django.shortcuts import redirect
from django.conf import settings
from django.http.response import JsonResponse


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
       


    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # Check if the user is authenticated and not on the login page
        if 'auth_code' in request.session:
            response = self.get_response(request)
            return response
   
        if request.path in  ['/polls','/authcode','/logout','/login','/','/profile'] :
        #csrf, redirect by upstox,redirect by the redirected url, login and logout 
            response = self.get_response(request)
            return response
    
       
        return JsonResponse({'error': 'Permission denied','url':'/login'},status=403)
        
            # Code to be executed for each request/response after
        # the view is called.

        