#coding:utf8
from django.contrib import admin

# Register your models here.
from models import Question,Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['question_text','pub_date']

    # 内容页字段详细配置
    fieldsets = [
        ('基本' , {'fields':['question_text']}),
        ('时间及其它' ,{'fields':['pub_date'] ,'classes':['collapse']}),
    ]
    # 列表页字段详细配置
    list_display = ('question_text','pub_date','was_published_recently')

    # 右侧字段过滤
    list_filter = ['pub_date']

    # 搜索字段
    search_fields = ['question_text']

    inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)
# admin.site.register(Choice)