from django.urls import path
from django.conf.urls import url
from tech_library.views import home
#add app urls here

urlpatterns = [url(r'^$',home,name="home"),]