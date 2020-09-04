# Generated by Django 2.2.10 on 2020-09-04 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ThesisPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thesis_title', models.CharField(max_length=60, null=True)),
                ('semester_name', models.CharField(max_length=60, null=True)),
                ('course_name', models.CharField(max_length=60, null=True)),
                ('course_code', models.CharField(max_length=60, null=True)),
                ('section', models.CharField(max_length=60, null=True)),
                ('description', models.TextField(max_length=255, null=True)),
                ('thesis_file', models.FileField(null=True, upload_to='files/Thesis/%Y/%m/%d/')),
                ('thumbnail', models.FileField(null=True, upload_to='thumbnail/%Y/%m/%d/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-uploaded_at',),
            },
        ),
        migrations.CreateModel(
            name='ProjectDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(blank=True, max_length=60, null=True)),
                ('semester_name', models.CharField(blank=True, max_length=60, null=True)),
                ('course_name', models.CharField(blank=True, max_length=60, null=True)),
                ('course_code', models.CharField(blank=True, max_length=60, null=True)),
                ('section', models.CharField(blank=True, max_length=60, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('project_file', models.FileField(blank=True, null=True, upload_to='files/projects/%Y/%m/%d/')),
                ('document', models.FileField(blank=True, null=True, upload_to='files/documents/%Y/%m/%d/')),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to='thumbnail/%Y/%m/%d/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-uploaded_at',),
            },
        ),
    ]
