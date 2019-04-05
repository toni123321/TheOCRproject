# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
#--- model for image ---
class Image(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='images/')
    current_user = models.ForeignKey(User,default=None)
    def __str__(self):
        return self.name
