from django.contrib import admin
from .models import Lesson

# Register your models here.
admin.site.register(Lesson)

class LessonAdmin(admin.ModelAdmin):
    class Meta:
        model = Lesson