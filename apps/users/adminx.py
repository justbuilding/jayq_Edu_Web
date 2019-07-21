# -*- coding: utf-8 -*-
__author__ = 'JackieQ'
__date__ = '2019/7/21 9:27'
import xadmin

from .models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    # 元组记得后面有逗号 list_display = (code,)
    # 在邮箱验证码显示相应列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 查,在书签旁增加搜索栏
    search_fields = ['code', 'email', 'send_type']
    # 想通过时间查找，需要增加过滤器
    list_filter = ['code', 'email', 'send_type', 'send_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)