from django.apps import AppConfig


class FnoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    usecaseslist = {'funds':{'api':'/user/get-funds-and-margin?segment=SEC'},
                    'trades':{'api':'/order/trades/get-trades-for-day'},
                    'positions':{'api':'/portfolio/short-term-positions'},
                    'open_positions':'open_positions',
                    'options_chain':{'api':'/option/chain'},
                    }
    name = 'fnoappbe'
      
    localdomain = 'http://127.0.0.1:8000'
    fedomain = 'http://127.0.0.1:3000' #for now because we don't know if azure will run react server
    proddomain = 'https://upstox-app.azurewebsites.net'
    sandboxclientid= '2f21b28b-6251-4c8e-861f-6218bdf7e4b6'
    prodclientid = 'cc982509-6fa9-4046-939d-41b190aa9252'
    sandboxclientsecret = 'ojruk78aqh'
    prodclientsecret =  '9t2r4lxi4z'
      
    UPSTOX_API = 'https://api.upstox.com/v2'
    domainsarray = { 'sandbox':   { 'name': 'sandbox','url':localdomain,'clientid':sandboxclientid,'clientsecret':sandboxclientsecret},
                       'prod': {'name':'prod', 'url': proddomain,'clientid':prodclientid,'clientsecret':prodclientsecret}
                    }
