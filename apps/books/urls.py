from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.new, name='new'),
    url(r'^create$', views.create, name='create'),
    url(r'^show/(?P<id>\d+)/$', views.show, name='show'),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
    url(r'^update/(?P<id>\d+)/$', views.update, name='update'),
]
