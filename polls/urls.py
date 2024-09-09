from django.urls import path

from . import views
from .viewclasses import *

urlpatterns = [
    #path("", defaultView.as_view(), name="defaultViewClass"),
    path("", views.index, name="index"),
    path("funds",funds.as_view(),name="fundsView"),
    path("optionsdata",optionsdata.as_view(),name="optionsdataView")

]