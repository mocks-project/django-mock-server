# Generated by Django 2.1.11 on 2019-11-29 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mocks', '0006_mocks_tenancy_aware_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mocks.Category'),
        ),
    ]