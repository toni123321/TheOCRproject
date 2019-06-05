from django.conf.urls import url
from . import views
from ocr_app.views import UserRegistrationView, UserLoginView, ProfileView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^register/$', view=UserRegistrationView.as_view(), name='register'),
    url(r'^success_register/$', views.success_register, name='success_register'),
    url(r'^login/$', view=UserLoginView.as_view(), name='login'),
    url(r'^logout/$', view=LogoutView.as_view(), name='logout'),
    url(r'^profile/$', view=ProfileView.as_view(), name='profile'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^list/$', views.list, name='list'),
    url(r'^current_image/(?P<id>[0-9]+)/$', views.current_image, name='current_image'),
]
