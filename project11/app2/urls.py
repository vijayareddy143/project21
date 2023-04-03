from django.urls import path
from app2.views import *
app_name='app2'

urlpatterns=[
    path('sai/',sai,name='sai'),
    path('chinni/',chinni,name='chinni'),
]