# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Dreamer(models.Model):
	fname = models.CharField(max_length=20)
	lname = models.CharField(max_length=20)
	email = models.EmailField()

class Dream(models.Model):
	dream = models.TextField()
	dreamer = models.ForeignKey(Dreamer)
	dreamt_on = models.DateTimeField(auto_now=True)