from django.apps import AppConfig


class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
    localdomain = 'http://127.0.0.1:8000/'
    UPSTOX_API = 'https://api.upstox.com/v2/'
    azuredomain = 'https://upstox-app.azurewebsites.net/'

