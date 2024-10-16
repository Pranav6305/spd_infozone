# members/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('batch/', views.batch_view, name='batch'),
    path('students/', views.student_list_view, name='student_list'),
    path('student/<str:roll_no>/', views.student_detail_view, name='student_detail'),
]
