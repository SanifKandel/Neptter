# Generated by Django 4.0.1 on 2022-06-26 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_likepost'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cover_pic',
            field=models.FileField(default='user.png', upload_to='uploads'),
        ),
    ]
