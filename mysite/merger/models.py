# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Merge(models.Model):
	MERGE_TYPE_CHOICES = (
			('merge','merge'),
			('deploy','deploy'),
		)
	MERGE_STATUS_CHOICES = (
			('raised','raised'),
			('viewed','viewed'),
			('started','started'),
			('failed','failed'),
			('resolved','resolved'),
		)
	merge_type = models.CharField(max_length=6,choices=MERGE_TYPE_CHOICES)
	merge_status = models.CharField(max_length=8,default="raised",choices=MERGE_STATUS_CHOICES)
	raised_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	resolved_on = models.DateTimeField()


class Comment(models.Model):
	content = models.CharField(max_length=255)
	added_on = models.DateTimeField(auto_now_add=True)