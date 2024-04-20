from django.contrib import admin
from .models import Student,AttendanceRecord,Report,Teacher
# Register your models here.
admin.site.register(Student)
admin.site.register(AttendanceRecord)
admin.site.register(Report)
admin.site.register(Teacher)


