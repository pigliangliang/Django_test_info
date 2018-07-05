"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,re_path
from people.views import UserView,resolv_client
from people import client_ip
import sys
import untitled1
from people.client_ip import process
sys.path.append('/untitled1/people/client_ip')

urlpatterns = [
    #使用反射机制，为djiango开发一套动态路由
    re_path('^(?P<app>(\w+))/(?P<function>(\w+))/$',process),
    path('admin/', admin.site.urls),
    path(r'',resolv_client.as_view()),
    re_path(r'^(?P<version>\w+)/users/$',UserView.as_view(),name='users')
]
