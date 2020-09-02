from django.contrib import admin
from django.urls import path,include
from serverresponse.api import views

from serverresponse.api.views import LNMonlineapiview

urlpatterns = [
    path('lnms/',LNMonlineapiview.as_view(), name='lnm-onlinecallbackurl'),


]


#urlpatterns = [
    #path("lnm/", LNMCal.as_view(), name="lnm-callbackurl"),
    #path("c2b-validation/", C2BValidationAPIView.as_view(), name="c2b-validation"),
    #path("c2b-confirmation/", C2BConfirmationAPIView.as_view(), name="c2b-confirmation"),

   # ]