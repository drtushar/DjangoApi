from django.db import models

# Create your models here.

class Himanshu(models.Model):
    name = models.CharField(max_length=10)
    some = models.CharField(max_length=10)
    idd = models.IntegerField()
    
    def __str__(self):
        return self.name
    