# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Branch, Merge, Comment

# Register your models here.
admin.site.register(Branch)
admin.site.register(Merge)
admin.site.register(Comment)