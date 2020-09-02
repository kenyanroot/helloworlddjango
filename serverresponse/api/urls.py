from django.contrib import admin
from django.urls import path,include
from serverresponse.api import views

from serverresponse.api.views import LNMonlineapiview

urlpatterns = [
    path('lnms/',LNMonlineapiview.as_view(), name='lnm-onlinecallbackurl'),


]