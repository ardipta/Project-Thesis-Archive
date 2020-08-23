from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student_dashboard/', views.student_choice, name='student_dashboard_choice'),
    path('student_dashboard/project_upload/', views.project_upload, name='project_upload'),
    path('student_dashboard/thesis_upload/', views.thesis_upload, name='thesis_upload'),
]
