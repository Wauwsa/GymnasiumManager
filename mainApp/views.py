from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Test, Subject, Absenzen
import datetime

# Create your views here.
# POST Logout muss nur in der View für Index getestet werden, da in HTML action="." --> Post wird zu root weitergeleitet


def main_page(request):
    if request.user.is_authenticated:  # if user is logged in
        if request.method == "POST":
            if request.POST['logout'] == 'logout':  # check if post is for logout
                logout(request)  # logout the user
                return redirect('loginForm:login')
        else:
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
        return render(request, 'noten.html', {'grades': grades})
    else:  # else redirect to login page
        return redirect('loginForm:login')


def absenzen(request):
    if request.user.is_authenticated:  # if user is logged in
        object_list = Subject.objects.order_by('name')
        subject_list = []
        for subject in object_list:
            subject_list.append(subject.name)
        absenzen_local = Absenzen.get_absenzen(student=request.user.id, subjects=subject_list)
        absenzen_sum_dict = {}
        for subject, absenz in absenzen_local.items():
            absenzen_sum = 0
            for absenz_list in absenz:
                if absenz_list['Entschuldigt'] == 'Nein':
                    absenzen_sum += 1
            absenzen_sum_dict[subject] = absenzen_sum
        return render(request, 'absenzen.html', {'absenzen': absenzen_local, 'absenzen_sum_dict': absenzen_sum_dict})
    else:  # else redirect to login page
        return redirect('loginForm:login')
