from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', (views.index)),
    url(r'^create$', (views.create)),
    url(r'^delete_page/(?P<id>\d*)$', views.delete_page),
]
