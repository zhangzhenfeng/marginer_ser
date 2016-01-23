from django.http.response import Http404
from django.shortcuts import render_to_response
from django.db import connection

def index(request):
    return render_to_response('main.html',{'name':'1'})