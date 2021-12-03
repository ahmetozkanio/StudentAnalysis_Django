from django import forms
from .models import Lesson,Attendance


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson

        # formda goruntulenecek alanlar
        fields = ["lesson_name","content"]

class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance

        # formda goruntulenecek alanlar
        fields = ["lesson","attendance_date"]

