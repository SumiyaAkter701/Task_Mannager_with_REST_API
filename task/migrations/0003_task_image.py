# Generated by Django 5.0.1 on 2024-01-28 07:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_task_completed_date_alter_task_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Task-Image')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='task.task')),
            ],
        ),
    ]
