from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .models import Subject, Absenzen, SchoolClass, Person, Grade
from .forms import NewTestForm, NewGradeForm, NewThemaForm
from django.contrib import messages

# Create your views here.
# POST Logout muss nur in der View für Index getestet werden, da in HTML action="." --> Post wird zu root weitergeleitet


def main_page(request):
    if request.user.is_authenticated:  # if user is logged in
        if request.method == "POST":
            if request.POST['logout'] == 'logout':  # check if post is for logout
                logout(request)  # logout the user
                return redirect('loginForm:login')
        else:
            recent_grades = Grade.get_recent_grades(student_id=request.user.id)
            return render(request, 'index.html', {'recent_grades': recent_grades})

    else:  # else redirect to login page
        return redirect('loginForm:login')


def noten(request):
    if request.user.is_authenticated:  # if user is logged in
        subject_list = Subject.get_subjects()
        grades = Grade.get_grades(student=request.user.id, subjects=subject_list)
        grades_sum_dict = Grade.get_avg_subject(grades=grades)
        return render(request, 'noten.html', {'grades_dict': grades, 'grades_sum_dict': grades_sum_dict})
    else:  # else redirect to login page
        return redirect('loginForm:login')


def absenzen(request):
    if request.user.is_authenticated:  # if user is logged in
        absenzen_local = Absenzen.get_absenzen(student=request.user.id)
        absenzen_sum_local = Absenzen.get_sum(absenzen_dict=absenzen_local)
        return render(request, 'absenzen.html', {'absenzen_dict': absenzen_local, 'absenzen_sum_dict': absenzen_sum_local})
    else:  # else redirect to login page
        return redirect('loginForm:login')


def panel(request):
    if request.user.is_authenticated:
        if request.user.is_teacher():
            if request.method == "POST":
                if request.POST.get('new-grade') == 'new-grade':
                    return redirect('mainApp:new-grade')
                elif request.POST.get('new-theme') == 'new-theme':
                    return redirect('mainApp:new-thema')
            klasse = SchoolClass.get_class_of_teacher(request.user.id)
            return render(request, 'panel.html', {'klasse': klasse})
        else:
            return redirect('mainApp:home')
    else:  # else redirect to login page
        return redirect('loginForm:login')


def klassen(request):
    if request.user.is_authenticated:
        if request.user.is_teacher():
            class_list = SchoolClass.get_classes()
            student_dict = SchoolClass.get_students_classes(class_names=class_list)
            return render(request, 'klassen.html', {'student_dict': student_dict})
        else:
            return redirect('mainApp:home')
    else:  # else redirect to login page
        return redirect('loginForm:login')


def detail(request, student_id):
    if request.user.is_authenticated:
        if request.user.is_teacher():
            student = get_object_or_404(Person, pk=student_id)
            recent_grades = Grade.get_recent_grades(student_id=student_id)
            return render(request, 'schuler.html', {'student': student, 'recent_grades': recent_grades})
        else:
            return redirect('mainApp:home')
    else:  # else redirect to login page
        return redirect('loginForm:login')


def new_grade(request):
    if request.user.is_authenticated:
        if request.user.is_teacher():
            if request.method == 'POST':
                if request.POST.get('new-grade-form') == 'new-grade':
                    form = NewGradeForm(current_user=request.user, data=request.POST)
                    if form.is_valid():
                        form.save()
                        messages.success(request, "Die Note wurde erfolgreich eingetragen!")
                    else:
                        messages.error(request, "Der Vorgang ist fehlgeschlagen, bitte versuchen Sie es erneut!")
            form = NewGradeForm(current_user=request.user)
            return render(request, 'new-grade.html', {'form': form})
        else:
            return redirect('mainApp:home')
    else:
        return redirect('loginForm:login')


def new_test(request):
    if request.user.is_authenticated:
        if request.user.is_teacher():
            if request.method == 'POST':
                if request.POST.get('new-test-form') == 'new-test':
                    form = NewTestForm(data=request.POST, current_user=request.user)
                    if form.is_valid():
                        form.save()
                        messages.success(request, "Der Test wurde erfolgreich erstellt!")
                        return redirect('mainApp:new-grade')
                    else:
                        messages.error(request, "Der Vorgang ist fehlgeschlagen, bitte versuchen Sie es erneut!")
            form = NewTestForm(current_user=request.user)
            return render(request, 'new-test.html', {'form': form})
        else:
            return redirect('mainApp:home')
    else:
        return redirect('loginForm:login')


def new_thema(request):
    if request.user.is_authenticated:
        if request.user.is_teacher():
            if request.method == 'POST':
                if request.POST.get('new-thema-form') == 'new-thema':
                    form = NewThemaForm(current_user=request.user, data=request.POST)
                    if form.is_valid():
                        form.save()
                        messages.success(request, "Das Thema wurde erfolgreich erstellt!")
                        next_site = request.POST.get('next', '/')
                        return redirect(next_site)
                    else:
                        messages.error(request, "Der Vorgang ist fehlgeschlagen, bitte versuchen Sie es erneut!")
            form = NewThemaForm(current_user=request.user)
            return render(request, 'new_thema.html', {'form': form})
        else:
            return redirect('mainApp:home')
    else:
        return redirect('loginForm:login')


def all_grades(request, student_id):
    if request.user.is_authenticated:
        if request.user.is_teacher():
            if request.method == 'POST':
                print('post')
                if 'delete' in request.POST:
                    print('delete')
                    Grade.objects.filter(pk=request.POST.get('delete')).delete()
            subject_list = Subject.get_subjects()
            grades = Grade.get_grades(student=student_id, subjects=subject_list)
            grades_sum_dict = Grade.get_avg_subject(grades=grades)
            student = get_object_or_404(Person, pk=student_id)
            return render(request, 'all_grades.html', {'grades_dict': grades, 'grades_sum_dict': grades_sum_dict, 'student': student})
        else:
            return redirect('mainApp:home')
    return redirect('loginForm:login')
