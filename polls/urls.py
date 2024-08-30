from django.urls import path

from . import views
from .viewclasses import defaultView

urlpatterns = [
    path("", defaultView.as_view(), name="defaultViewClass"),
    
]