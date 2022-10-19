from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Grade(models.Model):
    grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)])
    date = models.DateField()
