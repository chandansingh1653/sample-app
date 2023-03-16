from django.db import models

# Create your models here.
class Student(models.Model):
    first_Name = models.CharField(max_length=100)
    last_Name = models.CharField(max_length=100)
    batch = models.CharField(max_length=10)
    creation_date = models.DateField("creation_date")

    def __str__(self):
        return self.first_Name 


