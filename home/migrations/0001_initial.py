# Generated by Django 4.0.1 on 2022-06-19 19:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('pic', models.ImageField(blank=True, upload_to='uploads')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('tags', models.CharField(blank=True, max_length=100)),
                ('like', models.PositiveIntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=300, null=True)),
                ('profile_pic', models.FileField(default='user.png', upload_to='uploads')),
                ('birthday', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=2, null=True)),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
