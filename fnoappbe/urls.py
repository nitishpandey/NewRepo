from django.urls import path, re_path

from . import views
from .apis import *


urlpatterns = [
    path("",views.get_csrf_token, name="csrftoken"),
    path("predict", predictor.as_view(), name="predictor"),
    re_path(r'\b(funds|trades|options_chain|positions)\b',datafetch.as_view()),
    path("apicredentials", views.NotImplementedType, name="nothandled"),
    path("login", views.login, name="login"),
    
]