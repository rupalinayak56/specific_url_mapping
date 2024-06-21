from django.urls import path
from webseries.views import *
app_name="nothing"
urlpatterns=[
    path('songkong/',songkong,name='songkong'),
    path('heroine/',heroine,name='heroine'),
]