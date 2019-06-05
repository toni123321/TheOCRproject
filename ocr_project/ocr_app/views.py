# -*- coding: utf-8 -*-

# some imports
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from ocr_app.forms import UserRegistrationForm, LoginForm
from django.contrib.auth.views import LoginView
from .models import Image_m
from .forms import ImageForm
from . import forms

from PIL import Image
from pytesseract import image_to_string
import os
import tempfile
import subprocess
import pyttsx
#----- User registration views ----
class UserRegistrationView(CreateView):
    is_registered = False
    form_class = UserRegistrationForm
    template_name = "register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseForbidden()
        return super(UserRegistrationView, self).dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        success_url=('success_register')
        return redirect(success_url)


def success_register(request):
    return render(request, 'success_register.html')

#-----User login view -----
class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = "login.html"
    redirect_authenticated_user = True
    is_registered = True
    success_url = reverse_lazy('profile')

@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'profile.html'

    def dispatch(self, request, *args, **kwargs):
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

#---- Upload views ---

@login_required(login_url="/login/")
def upload(request):
    if request.method == 'POST':
        form = forms.ImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.current_user = request.user
            #image = Image_m.objects.get(instance.id)
            #instance.text = ocr(image.cover)
            instance.save()
            return redirect('list')
            #return render(request, 'current_image.html', {'image':image})
    else:
        form = forms.ImageForm()
    return render(request, 'upload_image.html', { 'form': form })


def list(request):
    images = Image_m.objects.all().filter(current_user = request.user)
    return render(request, 'list_images.html', {'images':images})


def ocr(path):
    image = Image.open(path, mode='r')
    return image_to_string(image)

def current_image(request, id):
    image = Image_m.objects.get(id=id)
    #text = ocr("../media/image/test.png")
    engine = pyttsx.init()
    text = str(ocr(image.cover)).replace("\n", " ")
    #output = engine.say(text)
    #output2 = engine.runAndWait()
    return render(request, 'current_image.html', {'text':text})

#home page
def index(request):
    return render(request, 'home.html')

#about page
def about(request):
    return render(request, 'about.html')
