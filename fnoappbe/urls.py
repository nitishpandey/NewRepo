from django.urls import path

from . import views

urlpatterns = [
    path("",views.get_csrf_token, name="csrftoken"),
    path("trades",views.emptyjson, name="empty_json"),

    path("login", views.login, name="login"),
    path("apicredentials", views.NotImplementedType, name="nothandled"),
    
]