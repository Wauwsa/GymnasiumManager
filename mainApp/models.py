from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.


class Student(AbstractUser):
    birth = models.DateField(default=datetime.date.today)
    street = models.CharField(max_length=25, blank=True, null=True)
    street_number = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    province = models.CharField(max_length=20, blank=True, null=True)
    code = models.IntegerField(validators=[MinValueValidator(0, MaxValueValidator(9999))], blank=True, null=True)

    def return_address(self):
        if self.birth and self.street and self.street_number and self.city and self.province and self.code:
            return self.street + ' ' + str(self.street_number) + ' ' + self.city + ' ' + str(self.code) + ' ' + self.province
        else:
            return 'N/A'

    def __str__(self):
        return f'{self.first_name + " " + self.last_name}'


class Test(models.Model):
    grade = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)])
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'Note: {self.grade}'


class Subject(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'
