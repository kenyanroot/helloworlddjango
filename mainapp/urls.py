"""mainapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import mpesaform, about, tecnologies
from .views import homepage, Viewclass







urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage,name='home'),
    path('api-auth/', include('rest_framework.urls')),
    path('Viewclass',Viewclass.as_view()),
    path('api/payments/' ,include("serverresponse.api.urls")),
    path('getstarted/' ,mpesaform ,name= 'mpesaform'),
    path('getstarted/Viewclass', Viewclass.as_view()),
    path('about',about, name= "about"),
    path('tecnologies',tecnologies, name="tecnologies"),

]
