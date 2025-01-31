from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('periodic-table/', views.periodic_table, name='periodic_table'),
] 