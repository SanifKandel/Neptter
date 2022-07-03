# Generated by Django 4.0.1 on 2022-07-02 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_rename_followerscount_followercount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Hawaa',
        ),
        migrations.RemoveField(
            model_name='followercount',
            name='user_id',
        ),
        migrations.AddField(
            model_name='followercount',
            name='profile_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.profile'),
        ),
    ]