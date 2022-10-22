from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
import datetime
# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth = models.DateField(default=datetime.date.today)
    street = models.CharField(max_length=25)
    street_number = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)])
    city = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    code = models.IntegerField(validators=[MinValueValidator(0, MaxValueValidator(9999))])

    def return_address(self):
        address = self.street + ' ' + str(self.street_number) + ' ' + self.city + ' ' + str(self.code) + ' ' + self.province
        return address

    def __str__(self):
        address = self.return_address()
        return f'Adresse: {address}'


class Test(models.Model):
    grade = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)])
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'Note: {self.grade}'


class Subject(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'
