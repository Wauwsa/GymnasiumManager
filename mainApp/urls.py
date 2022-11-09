from django.urls import path
from . import views

app_name = 'mainApp'
urlpatterns = [
    path('', views.main_page, name='home'),
    path('noten', views.noten, name='noten'),
    path('absenzen', views.absenzen, name='absenzen'),
    path('panel', views.panel, name='panel'),
    path('klassen', views.klassen, name='klassen'),
    path('schuler/<int:student_id>/', views.detail, name='detail')
]
