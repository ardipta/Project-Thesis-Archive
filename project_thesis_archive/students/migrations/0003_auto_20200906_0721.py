# Generated by Django 2.2.10 on 2020-09-06 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20200904_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='thesispaper',
            name='email',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='thesispaper',
            name='student_id',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='thesispaper',
            name='username',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
