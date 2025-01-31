from django.urls import path
from . import views

app_name = 'mentors'

urlpatterns = [
    path('', views.mentor_list, name='mentor_list'),
    path('detail/<int:mentor_id>/', views.mentor_detail, name='mentor_detail'),
    path('request/<int:mentor_id>/', views.request_mentor, name='request_mentor'),
] 