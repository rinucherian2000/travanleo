from django.db import models
from django.contrib.auth.models import User
from owner.models import Vaccin

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer", null=True)
    address = models.TextField(max_length=250)
    phone_no = models.CharField(max_length=10)


class AddToSolt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Vaccin, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True)
    options = (
        ("nonvaccinated", "nonvancinated"),
        ("process", "process"),
        ("cancel", "cancel"),
        ("vaccinated", "vancinated"),
    )
    status = models.CharField(max_length=120, choices=options, default="nonvancinated")