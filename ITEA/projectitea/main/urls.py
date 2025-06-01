from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('team/', views.team, name='team'),
    path('courses/', views.course, name='courses'),
    path('news/', views.news, name='news'),
    path('vacancies/', views.vacancy, name='vacancies'),
    
]