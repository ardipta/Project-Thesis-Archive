from django.db import models


class ProjectDocument(models.Model):
    project_name = models.CharField(max_length=60, null=True)
    semester_name = models.CharField(max_length=60, null=True)
    course_name = models.CharField(max_length=60, null=True)
    course_code = models.CharField(max_length=60, null=True)
    section = models.CharField(max_length=60, null=True)
    description = models.TextField(max_length=255, null=True)
    project_file = models.FileField(upload_to='files/projects/%Y/%m/%d/', null=True)
    document = models.FileField(upload_to='files/documents/%Y/%m/%d/', null=True)
    thumbnail = models.FileField(upload_to='thumbnail/%Y/%m/%d/', null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name


class ThesisPaper(models.Model):
    thesis_title = models.CharField(max_length=60, null=True)
    semester_name = models.CharField(max_length=60, null=True)
    course_name = models.CharField(max_length=60, null=True)
    course_code = models.CharField(max_length=60, null=True)
    section = models.CharField(max_length=60, null=True)
    description = models.TextField(max_length=255, null=True)
    thesis_file = models.FileField(upload_to='files/Thesis/%Y/%m/%d/', null=True)
    thumbnail = models.FileField(upload_to='thumbnail/%Y/%m/%d/', null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.thesis_title
