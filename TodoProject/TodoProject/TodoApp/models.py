from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class todoapp(models.Model):
    name=models.CharField(max_length=128)
    type=models.CharField(max_length=128)
    start_date=models.CharField(max_length=128)
    end_date=models.CharField(max_length=128)
    description=models.CharField(max_length=128)

    def __str__(self):
        return self.name

    user = models.ForeignKey(User, on_delete=models.CASCADE)
