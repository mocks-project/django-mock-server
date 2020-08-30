# Generated by Django 3.0.5 on 2020-08-17 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mocks', '0012_mock_null_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mock',
            name='path',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mocks', to='mocks.Endpoint'),
        ),
    ]