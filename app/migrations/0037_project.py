# Generated by Django 3.0.2 on 2020-02-03 13:40

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_delete_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(help_text='Title Of Project.', max_length=100)),
                ('url', models.CharField(help_text='<i>URL Address of the project.', max_length=10000)),
                ('unedited_image', models.ImageField(help_text='Image for project info (no edit when save).', storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\datoq_000\\Desktop\\Project/app/static/img/'), upload_to='')),
                ('image', models.ImageField(help_text="Project's Screenshot.<b style='color: red;'>Recommended Resolution For Image Is 1366x768!</b>", storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\datoq_000\\Desktop\\Project/app/static/img/'), upload_to='')),
                ('used_technologies', models.TextField(help_text='<b>write technologie names like : <i>HTML | CSS | Java | JavaScript</i>...</b>', max_length=1000)),
            ],
        ),
    ]
