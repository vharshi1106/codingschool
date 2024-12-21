from django.urls import path
from .views import *

app_name='app1'

urlpatterns=[
    path('',home,name="home"),
    path('home/',home,name="home"),
    path('courses/',courses,name="courses"),
    path('bootcamp/',bootcamp,name="bootcamp"),
    path('callback/',callback,name="callback"),
    path('signin/',signin,name="signin"),
]