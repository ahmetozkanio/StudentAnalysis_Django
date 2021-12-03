from django.contrib import admin
from .models import Lesson ,Attendance

# Register your models here.




@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["lesson_name","created_date"]
    class Meta:
        model = Lesson

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ["lesson","attendance_date","created_date"]
    list_filter = ["created_date",]
    search_field = ["lesson",]
    class Meta:
        model = ["lesson","created_date"]