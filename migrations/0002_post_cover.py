# Generated by Django 3.1.6 on 2021-02-16 17:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]
