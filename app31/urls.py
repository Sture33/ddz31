from django.urls import path

from app31 import views

urlpatterns = [
    path('', views.index, name='index')
]