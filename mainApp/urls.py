from django.urls import path
from . import views

app_name = 'mainApp'
urlpatterns = [
    path('', views.main_page, name='home'),
    path('noten', views.noten, name='noten'),
    path('absenzen', views.absenzen, name='absenzen'),
    path('panel', views.panel, name='panel'),
    path('klassen', views.klassen, name='klassen'),
    path('schuler/<int:student_id>/', views.detail, name='detail'),
    path('new-grade', views.new_grade, name='new-grade'),
    path('new-test', views.new_test, name='new-test'),
    path('new-thema', views.new_thema, name='new-thema'),
    path('schuler/noten/<int:student_id>/', views.all_grades, name='all_grades'),
    path('new-absenz', views.new_absenz, name='new-absenz'),
    path('schuler/absenzen/<int:student_id>/', views.all_absenzen, name='all_absenzen'),
]
