# -*- coding: utf-8 -*-

# some imports
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse

from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from ocr_app.forms import UserRegistrationForm, LoginForm
from django.contrib.auth.views import LoginView
# ---Main page views---

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
    #success_url = redirect('about')
    success_url = reverse_lazy('dashboard')



#home page
def index(request):
    return render(request, 'home.html')

#about page
def about(request):
    return render(request, 'about.html')
