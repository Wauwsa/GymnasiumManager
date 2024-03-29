from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser, Group
import datetime


# Create your models here.
class SchoolClass(models.Model):
    name = models.CharField(max_length=5)

    @staticmethod
    def get_students(class_name):
        student_list = []
        student_objects = Person.objects.filter(klasse__name=class_name)
        for student in student_objects:
            if student.is_student():
                student_dict = {}
                if student.first_name and student.last_name:
                    student_dict['Name'] = student.first_name + ' ' + student.last_name
                    student_dict['ID'] = student.id
                student_list.append(student_dict)
        return student_list

    @staticmethod
    def get_students_classes(class_names):
        students_dict = {}
        for class_name in class_names:
            student_list = SchoolClass.get_students(class_name)
            students_dict[class_name] = sorted(student_list, key=lambda d: d['Name'])
        return students_dict

    @staticmethod
    def get_class_of_teacher(teacher_id):
        try:
            teacher = Person.objects.select_related('klasse').get(pk=teacher_id)
        except Person.DoesNotExist:
            return None
        if teacher.is_teacher():
            students = teacher.klasse.get_students(teacher.klasse.name)
            sorted_students = sorted(students, key=lambda student: student['Name'])
            return {
                'Klasse': teacher.klasse.name,
                'Students': sorted_students
            }
        else:
            return None

    @staticmethod
    def get_classes():
        return SchoolClass.objects.order_by('name').values_list('name', flat=True).distinct()  # retrieves a list of class names directly, and uses the distinct() method to avoid duplicates

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'School Class'
        verbose_name_plural = "School Classes"


class Person(AbstractUser):
    klasse = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    birth = models.DateField(default=datetime.date.today)
    street = models.CharField(max_length=25, blank=True, null=True)
    street_number = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)], blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    province = models.CharField(max_length=20, blank=True, null=True)
    code = models.IntegerField(validators=[MinValueValidator(0, MaxValueValidator(9999))], blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super(Person, self).__init__(*args, **kwargs)
        if self.username and self.is_student() and not self.email and not self.first_name and not self.last_name:
            name = self.username.split('.')
            self.first_name = name[0].capitalize()
            self.last_name = name[len(name)-1].capitalize()
            self.email = f'{self.username}@stud.edubs.ch'
        elif self.username and self.is_teacher() and not self.email and not self.first_name and not self.last_name:
            name = self.username.split('.')
            self.first_name = name[0].capitalize()
            self.last_name = name[len(name)-1].capitalize()
            self.email = f'{self.username}@edubs.ch'

    def return_address(self):
        if self.street and self.street_number and self.city and self.province and self.code:
            return self.street + ' ' + str(self.street_number) + ' ' + self.city + ' ' + str(self.code) + ' ' + self.province
        else:
            return 'N/A'

    def get_age(self):
        return int((datetime.date.today() - self.birth).days / 365.25)

    def is_student(self):
        return self.groups.filter(name='Student').exists()

    def is_teacher(self):
        return self.groups.filter(name='Teacher').exists()

    def __str__(self):
        return f'{self.first_name + " " + self.last_name}'


class Subject(models.Model):
    teacher = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def get_subjects():
        return Subject.objects.order_by('name').values_list('name', flat=True).distinct()  # flat = True turns Tuple into flat list


class Thema(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    thema = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Thema'
        verbose_name_plural = 'Themen'

    def __str__(self):
        return f'{self.subject}, {self.thema}'


class Test(models.Model):
    thema = models.ForeignKey(Thema, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)  # need that to calculate average of class in one thema
    weight = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(99)], default=1)
    date = models.DateField(default=datetime.date.today)

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        if not self.school_class and request.user:
            self.school_class = request.user.klasse
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.thema.subject}, {self.thema.thema}, {self.school_class}'


class Grade(models.Model):
    student = models.ForeignKey(Person, on_delete=models.CASCADE)
    grade = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student}, {self.test.thema.subject}, {self.test.thema.thema}, {self.grade}'

    @staticmethod
    def get_grades(student, subjects):
        grades_dict_complete = {}
        for subject in subjects:
            grades_object_list = Grade.objects.filter(student=student, test__thema__subject__name=subject)
            grade_dict_list = []
            for grade in grades_object_list:
                grade_dict = {}
                grade_dict['Note'] = grade.grade
                grade_dict['Datum'] = grade.test.date.strftime('%d/%m/%Y')
                grade_dict['Thema'] = grade.test.thema
                grade_dict['Gewichtung'] = grade.test.weight
                grade_dict['ID'] = grade.id
                grade_dict_list.append(grade_dict)
            grades_dict_complete[subject] = grade_dict_list
        return grades_dict_complete

    @staticmethod
    def get_recent_grades(student_id):
        grades_list_complete = []
        grades_object_list = Grade.objects.filter(student_id=student_id).order_by('test__date')[:5]
        for grade in grades_object_list:
            grade_dict = {}
            grade_dict['Note'] = grade.grade
            grade_dict['Fach'] = grade.test.thema.subject
            grade_dict['Thema'] = grade.test.thema
            grade_dict['Datum'] = grade.test.date.strftime('%d/%m/%Y')
            grade_dict['Gewichtung'] = grade.test.weight
            grade_dict['ID'] = grade.id
            grades_list_complete.append(grade_dict)
        return grades_list_complete

    @staticmethod
    def get_avg_subject(grades):
        grades_sum_dict = {}
        for subject, subject_grades in grades.items():
            if len(subject_grades) != 0:  # if there are grades in this subject
                # Retrieve the weights for the grades in this subject
                weights = [grade['Gewichtung'] for grade in subject_grades]
                # Calculate the weighted sum of the grades
                weighted_sum = 0
                for i, grade in enumerate(subject_grades):
                    weighted_sum += grade['Note'] * weights[i]
                # Divide the weighted sum by the total weight to get the average
                grades_sum_dict[subject] = round(weighted_sum / sum(weights), 1)
        return grades_sum_dict


class Absenzen(models.Model):
    student = models.ForeignKey(Person, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    notes = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='absenzen/', blank=True, null=True)
    excused = models.BooleanField(default=False)

    def __str__(self):
        local_excuse = 'Ja' if self.excused else 'Nein'  # if self.excused == True set it to 'Ja'
        local_expire_date = self.date + datetime.timedelta(days=10)
        return f'{self.student.first_name}, {self.subject.name}, Entschuldigt: {local_excuse}, Abgabedatum: {local_expire_date}'

    class Meta:
        verbose_name = 'Absenz'
        verbose_name_plural = 'Absenzen'

    @staticmethod
    def get_absenzen(student, **kwargs):
        absenzen_dict_complete = {}
        object_list = Subject.objects.order_by('name')
        if kwargs:
            absenzen_object_list = Absenzen.objects.filter(student=student, pk=list(kwargs.values())[0]).order_by('excused', '-date')
            for absenz in absenzen_object_list:
                absenzen_dict = {}
                expire_date = absenz.date + datetime.timedelta(days=10)
                if absenz.excused:
                    absenzen_dict['Entschuldigt'] = 'Ja'
                elif not absenz.excused:
                    absenzen_dict['Entschuldigt'] = 'Nein'
                absenzen_dict['Abgabedatum'] = expire_date.strftime('%d/%m/%Y')
                current_date = datetime.date.today()
                if expire_date < current_date:
                    absenzen_dict['Abgelaufen'] = True
                else:
                    absenzen_dict['Abgelaufen'] = False
                absenzen_dict['ID'] = absenz.id
                if absenz.notes:
                    absenzen_dict['Notizen'] = absenz.notes
                if absenz.image:
                    absenzen_dict['Bild'] = absenz.image
                else:
                    absenzen_dict['Bild'] = False
                absenzen_dict['Fach'] = absenz.subject.name
                return absenzen_dict
        for subject in object_list:
            absenzen_list = []
            absenzen_object_list = Absenzen.objects.filter(student=student, subject__name=subject.name).order_by('excused', '-date')
            for absenz in absenzen_object_list:
                absenzen_dict = {}
                expire_date = absenz.date + datetime.timedelta(days=10)
                if absenz.excused:
                    absenzen_dict['Entschuldigt'] = 'Ja'
                elif not absenz.excused:
                    absenzen_dict['Entschuldigt'] = 'Nein'
                absenzen_dict['Abgabedatum'] = expire_date.strftime('%d/%m/%Y')
                current_date = datetime.date.today()
                if expire_date < current_date:
                    absenzen_dict['Abgelaufen'] = True
                else:
                    absenzen_dict['Abgelaufen'] = False
                absenzen_dict['ID'] = absenz.id
                if absenz.notes:
                    absenzen_dict['Notizen'] = absenz.notes
                if absenz.image:
                    absenzen_dict['Bild'] = absenz.image
                else:
                    absenzen_dict['Bild'] = False
                absenzen_list.append(absenzen_dict)
            absenzen_dict_complete[subject.name] = absenzen_list
        return absenzen_dict_complete

    @staticmethod
    def get_sum(absenzen_dict):
        absenzen_sum_dict = {}
        for subject, absenz in absenzen_dict.items():
            absenzen_sum = 0
            for absenz_list in absenz:
                if absenz_list['Entschuldigt'] == 'Nein' and not absenz_list['Abgelaufen']:  # alle unentschuldigten nicht abgelaufenen
                    absenzen_sum += 1
            absenzen_sum_dict[subject] = absenzen_sum
        return absenzen_sum_dict
