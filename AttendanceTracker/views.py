from django.shortcuts import render,redirect
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import Group
from . import forms
from .models import Student,AttendanceRecord
from django.views.decorators.csrf import csrf_protect


def home_view(request):
    return render(request, 'home.html')

def students_view(request):
    # Logic to retrieve and display student information
    return render(request, 'students.html')

# def attendance(request):
#     if request.method == 'POST':
#         # Logic to handle marking attendance
#         # This can include saving the attendance record to the database

#         # Redirect to the success page after marking attendance
#         return redirect('success_message')
#     else:
#         # Logic to retrieve and display student information
#         return render(request, 'attendance.html')
    




def success_message(request):
    return render(request, 'success_message.html')

def teachers(request):
    # Logic to retrieve and display teacher information
    return render(request, 'teachers.html')

from .models import AttendanceRecord  # Import the AttendanceRecord model

# @csrf_protect
# def attendance(request):
#     if request.method == 'POST':
#         # Logic to save attendance record, assuming you have implemented this
#         # For example:
#         student_name = request.POST.get('student_name')
#         course = request.POST.get('course')
#         date = request.POST.get('date')
#         status = request.POST.get('status')
#         AttendanceRecord.objects.create(student_name=student_name, course=course, date=date, status=status)
        
#     # Retrieve all attendance records
#     attendance_records = AttendanceRecord.objects.all()
    
#     # Pass the attendance_records to the reports.html template
#     return render(request, 'reports.html', {'attendance_records': attendance_records})
# from .models import AttendanceRecord

# def reports(request):
#     # Retrieve all attendance records from the database
#     attendance_records = AttendanceRecord.objects.all()

#     # Pass attendance records as context to the reports.html template
#     return render(request, 'reports.html', {'attendance_records': attendance_records})


def manage_students(request):
    # Add your logic for managing students
    return render(request, 'manage_students.html')

def manage_teachers(request):
    # Add your logic for managing teachers
    return render(request, 'manage_teachers.html')

def manage_attendance(request):
    # Add your logic for managing attendance
    return render(request, 'manage_attendance.html')

def generate_reports(request):
    # Add your logic for generating reports
    return render(request, 'generate_reports.html')


from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the attendance page upon successful login
            return redirect('attendance')  # Assuming 'attendance' is the name of the URL pattern for the attendance page
        else:
            # Return an invalid login error message
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')    
# views.py

# def student_signup_view(request):
#     userForm = forms.StudentUserForm()
#     studentForm = forms.StudentForm()
#     mydict = {'userForm': userForm, 'studentForm': studentForm} 
#     if request.method == 'POST':
#         userForm = forms.StudentUserForm(request.POST)
#         studentForm = forms.StudentForm(request.POST, request.FILES)
#         if userForm.is_valid() and studentForm.is_valid():
#             user = userForm.save()
#             user.set_password(user.password) 
#             user.save()

#             student = studentForm.save(commit=False)
#             student.user = user  
#             student.save()

#             my_student_group, _ = Group.objects.get_or_create(name='STUDENT')
#             my_student_group.user_set.add(user)
#             return HttpResponseRedirect('login')  # Redirect to login page after successful registration

#     return render(request, 'register.html', context=mydict)




def student_signup_view(request):
    userForm = forms.StudentUserForm()
    studentForm = forms.StudentForm()
    mydict = {'userForm': userForm, 'studentForm': studentForm} 
    if request.method == 'POST':
        userForm = forms.StudentUserForm(request.POST)
        customerForm = forms.StudentForm(request.POST, request.FILES)
        if userForm.is_valid() and studentForm.is_valid():
            user = userForm.save()
            user.set_password(user.password) 
            user.save()

            customer = studentForm.save(commit=False)
            customer.user = user  
            customer.save()

            my_customer_group, _ = Group.objects.get_or_create(name='STUDENT')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect(reverse('login') )
    return render(request, 'register.html', context=mydict)



from .models import Report  

def view_reports(request):
    # Retrieve reports from the database
    reports = Report.objects.all()  # You might want to filter or order reports as needed
    return render(request, 'reports.html', {'reports': reports})





# def adminlogin_view(request):
#     if request.method == 'POST':
#         # Handle form submission
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to admin panel upon successful login
#             return redirect('admin_panel')
#         else:
#             # Handle invalid login credentials
#             return render(request, 'adminlogin.html', {'error': 'Invalid username or password'})
#     else:
#         # Render the login page
#         return render(request, 'adminlogin.html')
    



from django.shortcuts import render, redirect
from .models import AttendanceRecord

def reports(request):
    # Retrieve all attendance records from the database
    attendance_records = AttendanceRecord.objects.all()
    return render(request, 'reports.html', {'attendance_records': attendance_records})



from django.shortcuts import render, redirect

# def mark_attendance(request):
#     # Logic to handle marking attendance
#     # This can include saving the attendance record to the database
    
#     # Redirect to the success page after marking attendance
#     return redirect('attendance_success')

# def view_attendance_report(request):
#     # Logic to retrieve and display attendance records from the database
#     # This can include querying the AttendanceRecord model
    
#     # Assuming you have attendance records available, pass them to the template
#     attendance_records = AttendanceRecord.objects.all()  # Change this query based on your model
    
#     return render(request, 'reports.html', {'attendance_records': attendance_records})

def attendance_success(request):
    return render(request, 'attendance_success.html')

def admin_base(request):
    return render(request, 'admin_base.html')


def attendance(request):
    attendanceRecordForm=forms.AttendanceRecordForm()
    if request.method=="POST":
        attendanceRecordForm=forms.AttendanceRecordForm(request.POST,request.FILES)
        if attendanceRecordForm.is_valid():
            attendanceRecordForm.save()
        return HttpResponseRedirect('/reports/')
    return render(request,'attendance.html',{'attendanceRecordForm':attendanceRecordForm})    




def attendance_reports(request):
    attendanceRecord = AttendanceRecord.objects.all()  # Query all attendance records
    return render(request, 'reports.html', {'attendanceRecord': attendanceRecord})


# views.py

from django.shortcuts import render, redirect
from .forms import TeacherForm
from .models import Teacher

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_message')  
    else:
        form = TeacherForm()
    return render(request, 'add_teachers.html', {'form': form})  
def teacher_details(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})

from django.shortcuts import render
from django.http import JsonResponse
from .models import AttendanceRecord




# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

def admin_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect('admin_base')  # Replace 'admin_dashboard' with your admin dashboard URL name
                else:
                    error_message = 'You do not have permission to access this page.'
            else:
                error_message = 'Invalid username or password.'
    else:
        form = LoginForm()
        error_message = None
    return render(request, 'adminlogin.html', {'form': form, 'error_message': error_message})



def afterlogin_view(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='customer').exists():
            return redirect('customer-home')
        else:
            return redirect('admin_base')  # Replace 'admin_base' with the appropriate URL name for admin dashboard
    else:
        return redirect('admin_login')  # Redirect to admin login if user is not authenticated

def adminclick_view(request):
    if request.method == 'POST':
        # Process form data, authenticate user, etc.
        # Assuming authentication is successful
        return redirect('afterlogin')  # or redirect to admin panel
    else:
        # Render the login form
        return render(request, 'adminlogin.html')

# def afterlogin_view(request):
#     if request.user.groups.filter(name='customer').exists():
#         return redirect('customer-home')
#     else:
#         return redirect('admin_pannel')
