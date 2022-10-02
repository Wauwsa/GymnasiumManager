from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('home', views.logged_in, name='home')
]