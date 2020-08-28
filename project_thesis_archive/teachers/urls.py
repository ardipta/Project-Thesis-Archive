from django.urls import path
from . import views

urlpatterns = [
    path('teacher_dashboard/', views.teacher_choice, name='teacher_dashboard_choice'),
    path('teacher_dashboard/teacher_show/', views.teacher_show, name='teacher_show_info'),
]
