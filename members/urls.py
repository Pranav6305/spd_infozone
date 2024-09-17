from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # The home (login) view
    path('batch/', views.batch_view, name='batch'),  # The batch view for batch.html
]
