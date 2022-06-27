from django.core import validators
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200, null=True, validators=[validators.MinLengthValidator(2)])
    category_description = models.TextField(null=True)
    created_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.category_name