from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('student_dashboard/', views.student_choice, name='student_dashboard'),
    path('student_dashboard/project_upload/', views.project_upload, name='project_upload'),
    path('student_dashboard/thesis_upload/', views.thesis_upload, name='thesis_upload'),
    path('student_dashboard/view_project_details/', views.view_project_details, name='view_project_details'),
    path('student_dashboard/view_thesis_details/', views.view_thesis_details, name='view_thesis_details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
