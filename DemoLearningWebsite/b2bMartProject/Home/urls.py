from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'homeAppUrls'


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^fromPage/(?P<var_from_page>[\s\w-]*)/$', views.home, name='fromPage'),
]
