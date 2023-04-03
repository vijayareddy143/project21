from django.urls import path
from app2.views import *
app_name='nothing'

urlpatterns=[
    path('prabha',prabha,name='prabha'),
]