#!/usr/bin/env python
# coding:utf-8

from django.db import models

# Create your models here.
class GBP_m15(models.Model):
	timeStamp = models.IntegerField(default=None)
	date = models.CharField(max_length= 20)
	time = models.CharField(max_length= 20)
	
	open = models.FloatField(default=None)
	high = models.FloatField(default=None)
	low = models.FloatField(default=None)
	close = models.FloatField(default=None)

	chinaTime = models.CharField(max_length= 20)

	#def __str__(self):
		#return self.province
