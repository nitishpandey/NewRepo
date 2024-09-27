from django.urls import path, re_path
from django.contrib import admin
from . import views
from .apis import *

urlpatterns = [
    path("",views.get_csrf_token, name="csrftoken"),
    path('admin/', admin.site.urls),
    path("polls", views.index, name="index"),
    path("authcode",  views.index, name="index"),
    path("logout", views.logout, name="logout"),
    path("login", views.login, name="login"),
    path("profile", views.profile, name="profile"),


    path("predict", predictor.as_view(), name="predictor"),
    re_path(r'\b(funds|trades|options_chain|positions)\b',datafetch.as_view()),
    path("apicredentials", views.NotImplementedType, name="nothandled"),
    
    
]