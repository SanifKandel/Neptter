# Generated by Django 4.0.1 on 2022-07-02 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_delete_hawaa_remove_followercount_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followercount',
            name='profile_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.profile'),
        ),
    ]
