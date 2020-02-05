# Generated by Django 3.0.2 on 2020-02-03 10:46

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_delete_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=10000)),
                ('image', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\datoq_000\\Desktop\\Project/app/static/img/'), upload_to='')),
                ('used_technologies', models.CharField(choices=[('item_key1', 'Item title 1.1'), ('item_key2', 'Item title 1.2'), ('item_key3', 'Item title 1.3'), ('item_key4', 'Item title 1.4'), ('item_key5', 'Item title 1.5')], max_length=100)),
            ],
        ),
    ]
