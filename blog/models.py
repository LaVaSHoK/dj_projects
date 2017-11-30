from django.db import models


class Users(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=32)
