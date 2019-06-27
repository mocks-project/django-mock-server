# Generated by Django 2.1.9 on 2019-06-27 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190623_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HeaderType',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='header',
            name='header_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.HeaderType'),
        ),
        migrations.AddField(
            model_name='header',
            name='mock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Mock'),
        ),
    ]