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
