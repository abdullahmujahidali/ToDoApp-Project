# Generated by Django 3.2.3 on 2021-05-18 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useend', '0003_alter_task_priority'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['priority']},
        ),
    ]
