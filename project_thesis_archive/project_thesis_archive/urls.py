from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('', include('students.urls')),
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),

]
