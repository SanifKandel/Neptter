# Generated by Django 4.0.1 on 2022-05-31 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.FileField(default='static/images/user.png', upload_to='static/uploads'),
        ),
    ]