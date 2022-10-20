from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.


class Test(models.Model):
    grade = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)])
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'Note: {self.grade}'
