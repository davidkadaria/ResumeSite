# Generated by Django 3.0.2 on 2020-02-02 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]