from django.contrib import admin
from students.models import ProjectDocument, ThesisPaper


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'semester_name', 'course_name', 'course_code', 'description', 'project_file',
                    'document']
    search_fields = ['project_name', 'semester_name', 'course_name', 'course_code', 'description']


class ThesisAdmin(admin.ModelAdmin):
    list_display = ['thesis_title', 'semester_name', 'course_name', 'course_code', 'description', 'thesis_file']
    search_fields = ['thesis_title', 'semester_name', 'course_name', 'course_code', 'description']


admin.site.register(ProjectDocument, ProjectAdmin)
admin.site.register(ThesisPaper, ThesisAdmin)
