from django.db import models
from django.contrib.contenttypes.models import ContentType
# Create your models here.
class DegreeCourse(models.Model):
    """
    学位课程
    """
    name = models.CharField(max_length=128,unique=True)

class Courese(models.Model):
    """
    普通课程
    """
    name = models.CharField(max_length=128,unique=True)

class Coupon(models.Model):
    """
    优惠券
    """
    name = models.CharField(max_length=64, verbose_name="活动名称")
    brief = models.TextField(blank=True, null=True, verbose_name="优惠券介绍")
    # course_type 代指哪张表
    course_type = models.ForeignKey(ContentType, blank=True, null=True,on_delete=models.CASCADE)
    # 代指对象ID
    object_id = models.IntegerField(blank=True, null=True)