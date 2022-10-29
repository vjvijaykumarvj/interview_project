from django.db import models

# Create your models here.

class Employee(models.Model):
    eno = models.IntegerField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    address  =models.CharField(max_length=200)

    def __str__(self):
        return self.name
