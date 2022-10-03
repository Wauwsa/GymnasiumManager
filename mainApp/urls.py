from django.urls import path
from . import views

# Create your views here.
app_name = 'mainApp'
urlpatterns = [
    path('', views.main_page, name='home'),
]