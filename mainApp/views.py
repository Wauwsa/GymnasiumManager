from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
# POST Logout muss nur in der View für Index getestet werden, da in HTML action="." --> Post wird zu root weitergeleitet


def main_page(request):
    if request.user.is_authenticated:  # if user is logged in
        if request.method == "POST":
            if request.POST['logout'] == 'logout':  # check if post is for logout
                print("About to logout")
                logout(request)  # logout the user
                return redirect('loginForm:login')
        else:
            return render(request, 'index.html', {})

    else:  # else redirect to login page
        return redirect('loginForm:login')


def noten(request):
    if request.user.is_authenticated:  # if user is logged in
        return render(request, 'noten.html')
    else:  # else redirect to login page
        return redirect('loginForm:login')


def absenzen(request):
    if request.user.is_authenticated:  # if user is logged in
        return render(request, 'absenzen.html')
    else:  # else redirect to login page
        return redirect('loginForm:login')
