from django.db import models
class Student (models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=200)
    birthday = models.DateTimeField()
