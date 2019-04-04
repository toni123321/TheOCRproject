# -*- coding: utf-8 -*-

# some imports
from __future__ import unicode_literals
from django.shortcuts import render

from django.views.generic import CreateView
from ocr_app.forms import UserRegistrationForm
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



#home page
def index(request):
    return render(request, 'home.html')

#about page
def about(request):
    return render(request, 'about.html')
