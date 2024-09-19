# members/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('batch/', views.batch_view, name='batch'),
    path('student/', views.student_view, name='student'),
]
