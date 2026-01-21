from django.urls import path
from . import views


urlpatterns = [
   path('', views.home_api, name='home_api'),
   path('students/', views.student_list, name='student_list'),
   path('students/<int:id>/', views.student_detail, name='student_detail'), 
]