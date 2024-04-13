from django.db import models


class User(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()


