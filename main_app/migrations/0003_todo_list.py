# Generated by Django 4.2.4 on 2023-09-14 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.list'),
            preserve_default=False,
        ),
    ]
