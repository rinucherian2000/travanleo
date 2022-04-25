from django.forms import ModelForm
from owner.models import Vaccin
from django import forms


class Vaccinform(ModelForm):
    class Meta:
        model = Vaccin
        fields = "__all__"

        widgets = {
            "district": forms.TextInput(attrs={"class": "form-control"}),
            "loction": forms.TextInput(attrs={"class": "form-control"}),
            "slot": forms.NumberInput(attrs={"class": "form-control"}),
            "date": forms.NumberInput(attrs={"class": "form-control"}),

        }