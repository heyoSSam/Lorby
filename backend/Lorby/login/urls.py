from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login),
    path('test_token', views.test_token),
]