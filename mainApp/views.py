from django.shortcuts import render, redirect
from django.contrib import messages
from loginForm.views import success

# Create your views here.


def main_page(request):
    global success
    print(success)
    if success:  # if variable is true, that means user just logged in
        messages.success(request, "You've successfully logged in!")  # success message
        success = False  # set success message to False
    return render(request, 'index.html', {})
