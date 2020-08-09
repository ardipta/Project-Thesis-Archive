from django.urls import path
from . import views

urlpatterns = [
    path('teacher_register/', views.teacher_reg_view, name='teacher_reg'),
    path('student_register/', views.student_reg_view, name='student_reg'),
    path('teacher_login/', views.teacher_login_view, name='teacher_login'),
    path('student_login/', views.student_login_view, name='student_login'),
]
