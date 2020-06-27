from django.urls import path
from django.urls import include, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    re_path(r'^search/', views.search, name='search')
]