from django import template
from ..models import Person, Grade
register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_class_button(local_dict, item):
    local_list = list(local_dict)
    if len(local_list) == 1:
        return 'collapsible bottom-collapsible top-collapsible'
    elif local_list.index(item) == 0:
        return 'collapsible top-collapsible'
    elif local_list.index(item) == len(local_list) - 1:
        return 'collapsible bottom-collapsible'
    return 'collapsible'


@register.filter
def get_average_all(student_id):
    grades_object_list = Grade.objects.filter(student__id=student_id)
    grades_list = []
    if grades_object_list:
        for grade in grades_object_list:
            grades_list.append(grade.grade)
        grades_list_sum = sum(grades_list)
        return round(grades_list_sum / len(grades_list), 1)
    return None


@register.filter
def get_avg_class(klasse, thema):
    if thema:
        grades_object_list = Grade.objects.filter(test__school_class=klasse, test__thema=thema)
        grades = []
        if thema and grades_object_list:
            for grade in grades_object_list:
                grades.append(grade.grade)
            return round(sum(grades) / len(grades), 1)
    return None


@register.filter
def get_number_students(klasse):
    if len(klasse) > 0:
        return len(klasse)
    return None


@register.filter
def get_teacher_of_class(klasse):
    members_objects = Person.objects.filter(klasse__name=klasse)
    for member in members_objects:
        if member.is_teacher():
            if member.first_name and member.last_name:
                return member.first_name + ' ' + member.last_name
            return None
        return None
