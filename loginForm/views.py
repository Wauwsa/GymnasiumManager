from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
global success
success = False  # success is variable if user has logged in successfully


def login_user(request):
    global success
    if request.method == "POST":  # if user goes to webpage and fills out form, do something
        uname = request.POST['uname']
        password = request.POST['password']
        user = authenticate(request, username=uname, password=password)
        if user is not None:
            login(request, user)
            success = True  # set the variable to True
            return redirect('mainApp:home')  # Redirect to a success page.
        else:
            messages.success(request, "The credentials are either wrong or that account does not exist.")
            return redirect('login')
    else:
        return render(request, 'login.html', {})
