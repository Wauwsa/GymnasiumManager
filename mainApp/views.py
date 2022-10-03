from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def main_page(request):
    if request.session['success']:  # if variable is true, that means user just logged in
        messages.success(request, "You've successfully been logged in!")  # success message
        request.session['success'] = False
    return render(request, 'index.html', {})
