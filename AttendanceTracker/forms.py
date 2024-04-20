# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Student,AttendanceRecord,Teacher

class StudentUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ()  # Add additional fields for student profile if needed


class AttendanceRecordForm(forms.ModelForm):
    class Meta:
        model = AttendanceRecord
        fields = ['student_name', 'course', 'date', 'status']



class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'phone_number']      



class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)          