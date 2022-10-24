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
        if self.street and self.street_number and self.city and self.province and self.code:
            return self.street + ' ' + str(self.street_number) + ' ' + self.city + ' ' + str(self.code) + ' ' + self.province
        else:
            return 'N/A'

    def get_age(self):
        return int((datetime.date.today() - self.birth).days / 365.25)

    def __str__(self):
        return f'{self.first_name + " " + self.last_name}'


class Subject(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class Test(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    grade = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(6)], blank=True, null=True)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'Note: {self.grade}'

    def get_grades(student, subjects):
        grades_dict = {}
        if type(subjects) == list:
            for subject in subjects:
                grades_list = []
                grades_object_list = Test.objects.filter(student=student, subject__name=subject)
                for grade in grades_object_list:
                    grades_list.append(grade.grade)
                grades_dict[subject] = grades_list
            return grades_dict
        else:
            grades_list = []
            grades_object_list = Test.objects.filter(student=student, subject__name=subjects)
            for grade in grades_object_list:
                grades_list.append(grade.grade)
            return grades_list


class Absenzen(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(default=datetime.date.today)
    excused = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        local_excuse = 'Ja' if self.excused else 'Nein'
        local_expire_date = self.date + datetime.timedelta(days=10)
        return f'{self.student.first_name}, {self.subject.name}, Entschuldigt: {local_excuse}, Abgabedatum: {local_expire_date}'

    def get_absenzen(student, subjects):
        absenzen_dict = {}
        for subject in subjects:
            absenzen_list_complete = []
            absenzen_object_list = Absenzen.objects.filter(student=student, subject__name=subject).order_by('-date')
            for absenz in absenzen_object_list:
                absenzen_list = []
                expire_date = absenz.date + datetime.timedelta(days=10)
                if absenz.excused:
                    absenzen_list.append('Ja')
                elif not absenz.excused:
                    absenzen_list.append('Nein')
                absenzen_list.append(expire_date.strftime('%d/%m/%Y'))
                absenzen_list_complete.append(absenzen_list)
            print(absenzen_list_complete)
            absenzen_dict[subject] = absenzen_list_complete
        print(absenzen_dict)
        return absenzen_dict
