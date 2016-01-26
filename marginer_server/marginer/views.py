# -*- coding: utf-8 -*-
from django.http.response import Http404
from django.shortcuts import render_to_response
from django.db import connection
from models import Info
from django.http import HttpResponse
import datetime

# 获取主页view
def index(request):
    return render_to_response('main.html',{})

# 获取树莓派信息
def get_sp_date(request):
    print '000000000'
    info = Info()
    sp_date_list = Info.objects.all()
    print '111111111111111'
    print(sp_date_list.filter(time__range=('2016-01-26', '2016-01-27')))
    print len(sp_date_list)
    return HttpResponse('')