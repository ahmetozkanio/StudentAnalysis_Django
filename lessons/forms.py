from django import forms
from .models import Lesson


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson

        # formda goruntulenecek alanlar
        fields = ["lesson_name",]
