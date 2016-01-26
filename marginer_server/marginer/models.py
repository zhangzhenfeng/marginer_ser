# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 树莓派信息表的model
class Info(models.Model):
    id=models.CharField(max_length=32,primary_key=True)
    temperature=models.CharField(max_length=10)
    humidity=models.CharField(max_length=10)
    cpu_temperature=models.CharField(max_length=10)
    cpu_rate=models.CharField(max_length=10)
    ram=models.CharField(max_length=20)
    disk=models.CharField(max_length=20)
    time=models.CharField(max_length=20)