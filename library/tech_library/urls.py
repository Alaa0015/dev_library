from django.urls import path
from django.conf.urls import url
from tech_library.views import home, display_dev
#add app urls here

urlpatterns = [
    url(r'^$',home,name="home"),
    url(r'^developers/$',display_dev,name="display_dev"),
    url(r'^developers/(\d+)$',display_dev,name="developer_detatils"),
    ]