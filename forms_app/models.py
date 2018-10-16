from django.db import models
from django.utils import timezone


class FormModel(models.Model):
    name = models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    date = models.DateField()
    budget = models.IntegerField
    employees = models.IntegerField

    def __str__(self):
        return self.name