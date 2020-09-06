from django.urls import path

from .views import LNMCallbackapiview

urlpatterns = [
    path('lnm/', LNMCallbackapiview.as_view(), name='lnm-callbackurl'),


]


#urlpatterns = [
    #path("lnm/", LNMCal.as_view(), name="lnm-callbackurl"),
    #path("c2b-validation/", C2BValidationAPIView.as_view(), name="c2b-validation"),
    #path("c2b-confirmation/", C2BConfirmationAPIView.as_view(), name="c2b-confirmation"),

   # ]