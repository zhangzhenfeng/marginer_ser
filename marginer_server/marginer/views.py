# -*- coding: utf-8 -*-
from django.http.response import Http404
from django.shortcuts import render_to_response
from django.db import connection,transaction
from models import Info
from django.http import HttpResponse
import datetime,time,json

# 获取主页view
def index(request):
    return render_to_response('main.html',{})

# 获取树莓派信息
def get_sp_date(request):
    # 获取当前日期
    date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    cursor = connection.cursor()
    query_sql = "select * from marginer_info where time like '%"+date+"%' order by time "
    cursor.execute(query_sql)    #执行sql语句
    all_info = cursor.fetchall()
    # 组织温度数据 {"cpu":[],"gpu":[],"house":[],"time":[]}
    temp_info = {"cpu":[],"gpu":[],"house":[],"humidity":[],"disk":[],"ram":[],"time":[]}
    for al in all_info:
        # 温度相关
        temp_info["time"].append(str(al[8])[-8:])
        temp_info["cpu"].append(al[3])
        temp_info["gpu"].append(al[4])
        temp_info["house"].append(al[1])
        
        # 湿度相关
        temp_info["humidity"].append(al[2])
        
        # 内存使用率
        temp_info["ram"].append(eval(al[6])[2]*100)
        
        # 磁盘使用率
        temp_info["disk"].append(al[7])
        
        
    return HttpResponse(json.dumps(temp_info), content_type="application/json")