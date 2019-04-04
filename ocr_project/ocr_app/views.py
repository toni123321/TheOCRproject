# -*- coding: utf-8 -*-

# some imports
from __future__ import unicode_literals
from django.shortcuts import render

# ---Main page views---

#home page
def index(request):
    return render(request, 'home.html')

#about page
def about(request):
    return render(request, 'about.html')
