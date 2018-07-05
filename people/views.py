from django.shortcuts import render,reverse
from django.http import HttpResponse
from  django.shortcuts import redirect,HttpResponse,resolve_url

# Create your views here.
from rest_framework.views import APIView
from rest_framework.versioning import QueryParameterVersioning
from rest_framework.versioning import URLPathVersioning

import json
import time


class resolv_client(APIView):
    def get(self,request,):
        ip=request.META['REMOTE_ADDR']
        username=request.user.username
        now_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        info={
            "ip":ip,
            "ip_locate":ip,
            "time":now_time,
            "owner":username,
            'status_code':200,

        }
        return HttpResponse(json.dumps(info))





class UserView(APIView):
    versioning_class = URLPathVersioning
    def get(self,request,*args,**kwargs):
        print(request.versioning_scheme.reverse(viewname='users',request=request))
        #request.version
        return HttpResponse(request.version)


def runpy():
    return ('hi,pig.')