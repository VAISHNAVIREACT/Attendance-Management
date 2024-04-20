# models.py
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class AttendanceRecord(models.Model):
    # Define model fields here
    student_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=1) 

class Report(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.student.username} - {self.course} - {self.date}"
    

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    # Add more fields as needed

    def __str__(self):
        return f"{self.first_name} {self.last_name}"    