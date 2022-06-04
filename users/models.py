from django.db import models

class UserDetails(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', unique=True, max_length=256)  # Field name made lowercase.
    fullname = models.TextField(db_column='FullName')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=256)  # Field name made lowercase.
    image = models.TextField(db_column='Image')  # Field name made lowercase.
    status = models.TextField(db_column='Status')  # Field name made lowercase.

    class Meta:
        db_table = 'user_details'
