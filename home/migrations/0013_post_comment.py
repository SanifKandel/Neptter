# Generated by Django 4.0.1 on 2022-07-01 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
