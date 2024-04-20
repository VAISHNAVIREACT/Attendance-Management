from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('students/', views.students_view, name='students'), 
    path('teachers/',views.teachers, name='teachers'),
    path('attendance/',views.attendance, name='attendance'),
    path('reports/',views.attendance_reports, name='reports'),
    # path('admin/manage_students/', views.manage_students, name='manage_students'),
    # path('admin/manage_teachers/', views.manage_teachers, name='manage_teachers'),
    # path('admin/manage_attendance/', views.manage_attendance, name='manage_attendance'),
    path('admin/generate_reports/', views.generate_reports, name='generate_reports'),
    path('register/login/', views.login_view, name='login'),
    path('register/', views.student_signup_view, name='register'),
    # path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('view-reports/', views.view_reports, name='view_reports'),    
    path('success_message/', views.success_message, name='success_message'),
    path('admin_base/', views.admin_base, name='admin_base'),
    path('teacher-details/', views.teacher_details, name='teacher_details'),
    path('add-teacher/', views.add_teacher, name='add_teacher'),
    path('adminclick/', views.adminclick_view, name='adminclick'),
    # path('afterlogin/', views.adminlogin_view, name='afterlogin'),
    path('admin-login/', views.admin_login, name='admin_login'),
    
    ]

