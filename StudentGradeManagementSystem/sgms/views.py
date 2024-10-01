from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student
from .forms import RegistrationForm
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Grade
from .forms import GradeForm
from .models import Attendance
from .forms import AttendanceForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Student.objects.create(user=user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'sgms/register.html', {'form': form})

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_grades')  # Redirect to the page where grades are viewed
    else:
        form = GradeForm()

    return render(request, 'add_grade.html', {'form': form})

def view_grades(request):
    grades = Grade.objects.all().values('assignment_name', 'score')
    return render(request, 'view_grades.html', {'grades': list(grades)})

def add_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AttendanceForm()
    return render(request, 'add_attendance.html', {'form': form})

def view_attendance(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'view_attendance.html', {'attendance_records': attendance_records})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'home.html')
