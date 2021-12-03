from django.contrib import admin
from django.urls import path
from lessons import views

app_name = "lessons"

urlpatterns = [
    path('',views.lessons, name ="lessons"),
    path('lesson/<int:id>',views.detail, name ="detail"),
    path('addlesson/',views.addLesson, name ="addlesson")
]