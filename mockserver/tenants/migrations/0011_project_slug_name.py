# Generated by Django 3.0.5 on 2020-07-25 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0010_project_tenants'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='record_name',
            field=models.SlugField(max_length=255, null=True),
        ),
    ]
