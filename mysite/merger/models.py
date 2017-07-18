# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Branch(models.Model):
	name = models.CharField(max_length=45)

	def __str__(self):
		return self.name

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
	branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
	repos = models.CharField(max_length=255)
	environment = models.CharField(max_length=255)
	merge_type = models.CharField(max_length=6,choices=MERGE_TYPE_CHOICES, default="merge")
	merge_status = models.CharField(max_length=8,default="raised",choices=MERGE_STATUS_CHOICES)
	raised_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	resolved_on = models.DateTimeField(null=True,blank=True)

	def __str__(self):
		return "branch: %s, repo: %s" % (self.branch,self.repos)


class Comment(models.Model):
	merge = models.ForeignKey(Merge, on_delete=models.CASCADE)
	content = models.CharField(max_length=255)
	added_on = models.DateTimeField(auto_now_add=True)

# b.merge_set.create(repos="proposalcp",environment="qc",merge_type="merge",)