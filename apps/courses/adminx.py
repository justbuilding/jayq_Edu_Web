# -*- coding: utf-8 -*-
__author__ = 'JackieQ'
__date__ = '2019/7/21 11:56'
import xadmin

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    # 元组记得后面有逗号 list_display = (code,)
    # 在邮箱验证码显示相应列
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students']
    # 查,在书签旁增加搜索栏
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    # 想通过时间查找，需要增加过滤器
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students']


# class BannerCourseAdmin(object):
#     list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students']
#     search_fields = ['name', 'desc', 'detail', 'degree', 'students']
#     list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students']
#     ordering = ['-click_nums']
#     readonly_fields = ['click_nums']
#     exclude = ['fav_nums']
#     inlines = [LessonInline, CourseResourceInline]
#
#     def queryset(self):
#         qs = super(BannerCourseAdmin, self).queryset()
#         qs = qs.filter(is_banner=True)
#         return qs


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    # 指定搜索外键的字段 course__name
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']
    model_icon = 'fa fa-film'


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
# xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)