from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.course_list, name="course_list"),
    path("detail/<int:id>", views.course_detail, name="course_detail"),
    path("lessons", views.course_lessons, name="course_lessons"),
]
