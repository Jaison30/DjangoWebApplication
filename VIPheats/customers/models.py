# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Gender(models.Model):
	name = models.CharField(max_length=10)

	def __unicode__(self):
		return self.name


class UserDetails(models.Model):
	name = models.ForeignKey(User)
	gender = models.ForeignKey(Gender)
	Age = models.DateTimeField()
	

	def __unicode__(self):
		return self.name
