from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=100, null=False)
    telephone = models.CharField(max_length=20)
    birthday = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
