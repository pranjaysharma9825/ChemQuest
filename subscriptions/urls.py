from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscription_plans, name='subscription_plans'),
    path('subscribe/<int:plan_id>/', views.subscribe, name='subscribe'),
] 