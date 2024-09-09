from django.apps import AppConfig


class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
    localdomain = 'http://127.0.0.1:8000/'
    sandboxclientid= '2f21b28b-6251-4c8e-861f-6218bdf7e4b6'
    prodclientid = 'cc982509-6fa9-4046-939d-41b190aa9252'
    sandboxclientsecret = 'ojruk78aqh'
    prodclientsecret =  '9t2r4lxi4z'
      
    UPSTOX_API = 'https://api.upstox.com/v2/'
    proddomain = 'https://upstox-app.azurewebsites.net/'
    domainsarray = [    { 'name': 'sandbox','url':localdomain},
                        {'name':'prod', 'url': proddomain},
                     ]
      

