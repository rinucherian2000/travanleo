from django.db import models

# Create your models here.


class Vaccin(models.Model):
    district= models.CharField(max_length=120, unique=True)
    loction= models.CharField(max_length=120, unique=True)
    slot = models.PositiveIntegerField(default=50)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.district