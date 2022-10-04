from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.


def login_user(request):
    if not request.user.is_authenticated:  # check if user is logged in already
        if request.method == "POST":  # if user goes to webpage and fills out form, do something
            uname = request.POST['uname']
            password = request.POST['password']
            user = authenticate(request, username=uname, password=password)
            if user is not None:
                login(request, user)
                request.session['success'] = True  # creates variable 'success' which can be used between sessions & assigns value True
                return redirect('mainApp:home')  # Redirect to a success page.
            else:
                messages.success(request, "The credentials are either wrong or that account does not exist.")
                return redirect('loginForm:login')
        else:
            return render(request, 'login.html', {})
    else:
        return redirect('mainApp:home')
