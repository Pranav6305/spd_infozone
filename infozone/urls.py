"""
URL configuration for infozone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# infozone/urls.py
from django.urls import path
from members import views

urlpatterns = [
    path('', views.home_view, name='home'),        # Root URL
    path('batch/', views.batch_view, name='batch'),  # Batch view
    path('student/', views.student_view, name='student'),  # Student view
]

