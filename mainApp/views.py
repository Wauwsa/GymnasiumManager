from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Test, Subject, Absenzen, SchoolClass

# Create your views here.
# POST Logout muss nur in der View für Index getestet werden, da in HTML action="." --> Post wird zu root weitergeleitet


def main_page(request):
    if request.user.is_authenticated:  # if user is logged in
        if request.method == "POST":
            if request.POST['logout'] == 'logout':  # check if post is for logout
                logout(request)  # logout the user
                return redirect('loginForm:login')
        else:
            print(SchoolClass.get_students('2a'))
            return render(request, 'index.html', {})

    else:  # else redirect to login page
        return redirect('loginForm:login')


def noten(request):
    if request.user.is_authenticated:  # if user is logged in
        object_list = Subject.objects.order_by('name')
        subject_list = []
        for subject in object_list:
            subject_list.append(subject.name)
        grades = Test.get_grades(student=request.user.id, subjects=subject_list)
        grades_sum_dict = Test.get_avg(grades=grades)
        return render(request, 'noten.html', {'grades': grades, 'grades_sum_dict': grades_sum_dict})
    else:  # else redirect to login page
        return redirect('loginForm:login')


def absenzen(request):
    if request.user.is_authenticated:  # if user is logged in
        absenzen_local = Absenzen.get_absenzen(student=request.user.id)
        absenzen_sum_local = Absenzen.get_sum(absenzen_dict=absenzen_local)
        return render(request, 'absenzen.html', {'absenzen': absenzen_local, 'absenzen_sum_dict': absenzen_sum_local})
    else:  # else redirect to login page
        return redirect('loginForm:login')


def panel(request):
    if request.user.is_authenticated:
        if request.user.is_teacher():
            return render(request, 'panel.html')
        else:
            return redirect('mainApp:home')


def klassen(request):
    if request.user.is_authenticated:
        if request.user.is_teacher():
            class_list = SchoolClass.get_classes()
            student_dict = SchoolClass.get_students(class_names=class_list)
            return render(request, 'klassen.html', {'student_dict': student_dict})
        else:
            return redirect('mainApp:home')
