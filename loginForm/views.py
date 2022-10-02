from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
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
            return redirect('home')  # Redirect to a success page.
        else:
            messages.success(request, "The credentials are either wrong or that account does not exist.")
            return redirect('login')
    else:
        return render(request, 'registration/login.html', {})


def logged_in(request):
    global success
    if success:  # if variable is true, that means user just logged in
        messages.success(request, "You've successfully logged in!")  # success message
        success = False  # set success message to False
    return render(request, 'index.html', {})
