# Generated by Django 4.0.1 on 2022-06-26 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_profile_cover_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, default='Nothing', max_length=255),
        ),
    ]
