from django.urls import path
from . import views


app_name = 'loginForm'
urlpatterns = [
    path('', views.login_user, name='login'),
]
