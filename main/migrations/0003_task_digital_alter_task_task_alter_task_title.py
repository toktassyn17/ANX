# Generated by Django 4.0.2 on 2022-03-31 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_task_options_task_email_task_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='digital',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.TextField(verbose_name='Definition'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
    ]
