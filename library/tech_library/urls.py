from django.urls import path
from django.conf.urls import url
from tech_library.views import home, display_dev, display_dev_details, display_themes, display_themes_details, display_topic_details
#add app urls here

urlpatterns = [
    url(r'^$',home,name="home"),
    url(r'^developers/$',display_dev,name="display_dev"),
    url(r'^themes/$',display_themes,name="display_themes"),
    url(r'^developers/(\d+)$',display_dev_details,name="developer_detatils"),
    url(r'^themes/(\d+)$',display_themes_details,name="display_themes_details"),
    url(r'^topics/(\d+)$',display_topic_details,name="display_topic_details"),
    ]