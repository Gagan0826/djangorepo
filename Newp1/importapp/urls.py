from .views import *

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("",fun1,name="function1")
]