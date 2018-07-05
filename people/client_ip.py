#author_by zhuxiaoliang
#2018-07-04 下午10:42
from django.http import HttpResponse
from django.shortcuts import reverse,redirect
import time
#python反射机制
def process(request,**kwargs):

    app = kwargs.get('app','people')
    function = kwargs.get('function','UserView')
    try:
        appobj = __import__("{}.views".format(app))
        viewobj = getattr(appobj,'views')
        funcobj = getattr(viewobj,function)
        ret = funcobj()
    except (ImportError,AttributeError) as e:
        return HttpResponse("404 Not Found")
    except Exception as e:
        return redirect(reverse('users'))
    return HttpResponse(ret)