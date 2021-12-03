from django.shortcuts import render,redirect ,get_object_or_404

from lessons.forms import LessonForm, AttendanceForm
from django.contrib import messages

from .models import Lesson
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

def lessons(request):
        
    keyword = request.GET.get("keyword")
    if keyword:
            lessons = Lesson.objects.filter(title__contains=keyword)
            # sadece aramalarda cikan article lar gelecek
            return render(request, "lessons.html", {"lessons": lessons})

    
    lessons = Lesson.objects.all()
    return render(request, "lessons.html", {"lessons": lessons})


def detail(request, id):
    # lesson = Lesson.objects.filter(id = id ).first()#ilk elemani aldik filter liste halinde getiriyor
    # id var ise getir yoksa 404 getir
    lesson = get_object_or_404(Lesson, id=id)

    # Comment yorum alani related_name = comments ile erisiyoruz
    # comments = lesson.comments.all()

    form = AttendanceForm(request.POST or None)

    if form.is_valid():

        attendance = form.save(commit=False)
        # Hangi Kullanici Giris yapmissa
        attendance.author = request.user

        attendance.save()
        messages.success(request,"Yoklama Olusturuldu")
        
    return render(request, "detail.html", {"lesson": lesson,"form_attendance":form})
