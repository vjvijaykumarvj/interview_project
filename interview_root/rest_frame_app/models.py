from django.db import models

# Create your models here.


class Database(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile_number = models.IntegerField()
    region_code = models.IntegerField()
    profile_picture = models.ImageField(upload_to='media')
    date_of_birth = models.DateField(max_length=8)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name