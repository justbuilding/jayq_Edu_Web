# _*_ encoding:utf-8 _*_
# 官方库
from __future__ import unicode_literals
from datetime import datetime

# 第三方库
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# 自定义userprofile覆盖默认的user表
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(("male", u"男"), ("female", u"女")), default="female")
    address = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


# 邮箱验证码
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(verbose_name=u"验证码类型", choices=(("register", u"注册"), ("forget", u"找回密码")), max_length=30)
    # 注意把datetime.now()的括号去掉，不然他会根据EmailVerifyRecord编译生成时间，而不是根据class实例化生成时间
    send_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.now)

    class Meta:
        # verbose_name是显示在xadmin的名称
        verbose_name = u"邮箱验证码"
        # verbose_name_plural指定了复数形式，不然网页会自动显示：邮箱验证码s
        verbose_name_plural = verbose_name

    # 使邮箱验证码显示出列表每行名称 	,格式为  admin222e(asdf@dasf.com) 而不是显示EmailVerifyRecord
    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)


# 轮播图
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y%m", verbose_name=u"轮播图", max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name
