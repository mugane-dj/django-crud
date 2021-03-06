from django.db import models

from email.policy import default
from weakref import proxy
from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.


# A Position is a title.
class Position(models.Model):
    title = models.CharField(max_length=50)

    # Return title
    def __str__(self):
        return self.title


class Gender(models.Model):
    gender_form = models.CharField(max_length=15)

    def __str__(self):
        return self.gender_form


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=4)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    base_pay = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', default=0)
    bonus = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', default=0)

