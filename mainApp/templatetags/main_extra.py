from django import template
from ..models import Test
register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


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
