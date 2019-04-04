# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
#home page
def index(request):
    return render(request, 'home.html')
