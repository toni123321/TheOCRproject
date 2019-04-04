from django.conf.urls import url
from . import views
from ocr_app.views import UserRegistrationView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^register/$', view=UserRegistrationView.as_view(), name='register'),
    url(r'^success_register/$', views.success_register, name='success_register'),
]
