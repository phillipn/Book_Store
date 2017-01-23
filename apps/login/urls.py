from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.form, name='form'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^users/(?P<user_id>\d+)/$', views.profile, name='profile')
]
