# Generated by Django 4.1.3 on 2022-12-06 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_alter_job_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
