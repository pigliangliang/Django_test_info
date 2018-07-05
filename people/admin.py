from django.contrib import admin

# Register your models here.
from .models import Courese,DegreeCourse,Coupon
admin.site.register(Coupon)
admin.site.register(DegreeCourse)
admin.site.register(Courese)