from django.urls import path

from . import views

app_name = 'authentication'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.logIntoSite, name='logIntoSite'),
    path('register', views.register, name='register'),
]
