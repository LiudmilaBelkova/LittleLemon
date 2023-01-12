from django.db import models

class UserComments(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    comment = models.CharField(max_length=1000)
