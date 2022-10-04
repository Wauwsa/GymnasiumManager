from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.


def main_page(request):
    if request.user.is_authenticated:  # if user is logged in
        try:
            request.session['success']
        except KeyError:
            request.session['success'] = False
        if request.session['success']:  # if variable is True, that means user just logged in
            messages.success(request, "You've successfully been logged in!")  # success message
            request.session['success'] = False  # set value to False again

        if request.method == "POST":
            if request.POST['logout'] == 'logout':  # check if post is for logout
                logout(request)  # logout the user
                return redirect('loginForm:login')
        else:
            return render(request, 'index.html', {})

    else:  # else redirect to login page
        return redirect('loginForm:login')
