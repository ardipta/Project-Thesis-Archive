from django.db import models


class ProjectDocument(models.Model):
    project_name = models.CharField(max_length=60)
    semester_name = models.CharField(max_length=60)
    course_name = models.CharField(max_length=60)
    course_code = models.CharField(max_length=60)
    section = models.CharField(max_length=60)
    description = models.TextField(max_length=255)
    project_file = models.FileField(upload_to='media/files/projects/%Y/%m/%d/')
    document = models.FileField(upload_to='files/documents/%Y/%m/%d/')
    thumbnail = models.FileField(upload_to='thumbnail/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name


class ThesisPaper(models.Model):
    thesis_title = models.CharField(max_length=60)
    semester_name = models.CharField(max_length=60)
    course_name = models.CharField(max_length=60)
    course_code = models.CharField(max_length=60)
    section = models.CharField(max_length=60)
    description = models.TextField(max_length=255)
    thesis_file = models.FileField(upload_to='files/Thesis/%Y/%m/%d/')
    thumbnail = models.FileField(upload_to='thumbnail/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.thesis_title
