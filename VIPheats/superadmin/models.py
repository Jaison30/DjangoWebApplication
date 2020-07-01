# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Materials(models.Model):
	name = models.CharField(max_length=50)
	category = models.ForeignKey(Category)
	price = models.IntegerField(null=False,blank=False)
	created_at = models.DateTimeField(auto_now_add=True)
	description = models.TextField()
	image = models.FileField(upload_to='static/images')

	def __str__(self):
		return self.name




