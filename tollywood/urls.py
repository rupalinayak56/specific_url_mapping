from django.urls import path
from tollywood.views import *
app_name="everything"
urlpatterns=[
    path('thallapathy/',thallapathy,name='thallapathy'),
    path('heroine/',heroine,name='heroine'),
]