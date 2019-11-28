# Generated by Django 2.1.11 on 2019-11-16 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mocks', '0004_mock_params_onetoone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='mock',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content', to='mocks.Mock'),
        ),
    ]