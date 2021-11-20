from django.contrib import admin
from django.urls import path
from lessons import views

app_name = "lessons"

urlpatterns = [
    path('',views.addLesson, name ="lessons")
]