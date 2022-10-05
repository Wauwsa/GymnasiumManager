from django.urls import path
from . import views

app_name = 'mainApp'
urlpatterns = [
    path('', views.main_page, name='home'),
    path('noten', views.noten, name='noten'),
    path('absenzen', views.absenzen, name='absenzen'),
]
