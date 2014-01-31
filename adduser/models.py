# Create your models here.
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50,
                                  blank=False)
    last_name = models.CharField(max_length=50,
                                 blank=True)
    email = models.EmailField(max_length=200,
                              blank=True)
    def __str__(self):
        return self.first_name