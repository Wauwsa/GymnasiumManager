from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Subject, Student

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
        for instance in object_list:
            subject_list.append(instance.name)
        return render(request, 'noten.html', {'subject_list': subject_list})
    else:  # else redirect to login page
        return redirect('loginForm:login')


def absenzen(request):
    if request.user.is_authenticated:  # if user is logged in
        return render(request, 'absenzen.html')
    else:  # else redirect to login page
        return redirect('loginForm:login')
