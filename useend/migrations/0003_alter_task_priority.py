# Generated by Django 3.2.3 on 2021-05-18 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useend', '0002_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')], max_length=128),
        ),
    ]
