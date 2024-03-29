# -*- coding: utf-8 -*-
__author__ = 'JackieQ'
__date__ = '2019/7/21 9:27'
import xadmin
from xadmin import views

from .models import EmailVerifyRecord,Banner


# 设置开启主题功能
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


# 修改标题和底部栏
class GlobalSettings(object):
    site_title = "慕课后台管理系统"
    site_footer = '慕课在线网'
    # 设置自动收起详细app栏
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    # 元组记得后面有逗号 list_display = (code,)
    # 在邮箱验证码显示相应列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 查,在书签旁增加搜索栏
    search_fields = ['code', 'email', 'send_type']
    # 想通过时间查找，需要增加过滤器
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    # 元组记得后面有逗号 list_display = (code,)
    # 在邮箱验证码显示相应列
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    # 查,在书签旁增加搜索栏
    search_fields = ['title', 'image', 'url', 'index']
    # 想通过时间查找，需要增加过滤器
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

