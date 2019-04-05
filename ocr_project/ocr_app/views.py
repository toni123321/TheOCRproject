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
from .models import Image
from .forms import ImageForm
from . import forms

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
            instance.save()
            return redirect('list')
    else:
        form = forms.ImageForm()
    return render(request, 'upload_image.html', { 'form': form })

def list(request):
    images = Image.objects.all().filter(current_user = request.user)
    return render(request, 'list_images.html', {'images':images})


#home page
def index(request):
    return render(request, 'home.html')

#about page
def about(request):
    return render(request, 'about.html')
