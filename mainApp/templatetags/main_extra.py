from django import template
from ..models import Test
register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_class_button(local_dict, item):
    local_list = list(local_dict)
    if local_list.index(item) == 0:
        return 'collapsible top-collapsible'
    elif local_list.index(item) == len(local_list) - 1:
        return 'collapsible bottom-collapsible'
    return 'collapsible'


@register.filter
def get_average_all(student_id):
    grades_object_list = Test.objects.filter(student__id=student_id)
    grades_list = []
    if grades_object_list:
        for grade in grades_object_list:
            grades_list.append(grade.grade)
        grades_list_sum = sum(grades_list)
        return round(grades_list_sum / len(grades_list), 1)
    return None


@register.filter
def get_avg_class(klasse, thema):
    grades_object_list = Test.objects.filter(school_class=klasse, thema=thema)
    grades = []
    if grades_object_list:
        for grade in grades_object_list:
            grades.append(grade.grade)
        return sum(grades) / len(grades)
    return None
