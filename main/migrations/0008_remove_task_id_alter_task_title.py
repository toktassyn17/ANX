# Generated by Django 4.0.4 on 2022-04-22 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_task_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='id',
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Title'),
        ),
    ]
