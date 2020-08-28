from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('student_dashboard/', views.student_choice, name='student_dashboard'),
    path('student_dashboard/project_upload/', views.project_upload, name='project_upload'),
    path('student_dashboard/thesis_upload/', views.thesis_upload, name='thesis_upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
