from django.forms import ModelForm
from .models import Grade, Person, Test, Thema, Subject, Absenzen


# create a form
class NewGradeForm(ModelForm):
    def __init__(self, current_user, *args, **kwargs):
        super(NewGradeForm, self).__init__(*args, **kwargs)
        self.fields['student'].queryset = Person.objects.filter(klasse=current_user.klasse.id).exclude(pk=current_user.id).order_by('username')
        self.fields['test'].queryset = Test.objects.filter(thema__subject__teacher=current_user).order_by('date')

    class Meta:
        model = Grade
        fields = ['student', 'test', 'grade']
        labels = {
            'student': 'Schüler',
            'test': 'Prüfung',
            'grade': 'Note',
        }
        help_texts = {
            'grade': 'Die Note muss zwischen 1 und 6 sein'
        }


class NewTestForm(ModelForm):
    def __init__(self, current_user, *args, **kwargs):
        super(NewTestForm, self).__init__(*args, **kwargs)
        self.fields['thema'].queryset = Thema.objects.filter(subject__teacher=current_user).order_by('-created_at')

    class Meta:
        model = Test
        fields = ['thema', 'school_class', 'weight', 'date']
        labels = {
            'thema': 'Thema',
            'school_class': 'Klasse',
            'weight': 'Gewichtung',
            'date': 'Datum'
        }


class NewThemaForm(ModelForm):
    def __init__(self, current_user, *args, **kwargs):
        super(NewThemaForm, self).__init__(*args, **kwargs)
        self.fields['subject'].queryset = Subject.objects.filter(teacher=current_user)

    class Meta:
        model = Thema
        fields = '__all__'
        labels = {
            'subject': 'Fach',
            'thema': 'Thema'
        }


class NewAbsenzForm(ModelForm):
    def __init__(self, current_user, *args, **kwargs):
        super(NewAbsenzForm, self).__init__(*args, **kwargs)
        self.fields['student'].queryset = Person.objects.filter(klasse=current_user.klasse.id).exclude(pk=current_user.id).order_by('first_name')
        self.fields['subject'].queryset = Subject.objects.filter(teacher=current_user)

    class Meta:
        model = Absenzen
        fields = '__all__'
        labels = {
            'student': 'Schüler',
            'subject': 'Fach',
            'date': 'Datum',
        }
