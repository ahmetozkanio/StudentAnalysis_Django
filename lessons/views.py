from django.shortcuts import render,redirect

from lessons.forms import LessonForm
from django.contrib import messages

# Create your views here.


def addLesson(request):
    # Form Kayit
    # request.POST bizim yazi alanlarimizi yukler

    form = LessonForm(request.POST or None)

    if form.is_valid():

        lesson = form.save(commit=False)
        # Hangi Kullanici Giris yapmissa
        lesson.author = request.user

        lesson.save()
        messages.success(request,"Basariyla Ders Olusturuldu")
        return redirect("index")
    return render(request,"addlesson.html",{"form":form})