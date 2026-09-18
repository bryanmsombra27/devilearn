from django.shortcuts import render
from .models import Course
# Create your views here.
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound


def course_list(request):
    courses = Course.objects.all()
    query = request.GET.get("q")

    if query:
        courses = courses.filter(
            Q(title__icontains=query) |
            Q(owner__first_name__icontains=query)
        )
    paginator = Paginator(courses, 8)
    page_number = request.GET.get("page")
    courses_obj = paginator.get_page(page_number)

    query_params = request.GET.copy()

    if "page" in query_params:
        query_params.pop("page")

    query_string = query_params.urlencode()

    return render(request, 'courses/courses.html', {
        "courses_obj": courses_obj,
        "query": query,
        "query_string": query_string
    })


def course_detail(request, slug):
    # course = [course.id == id for course in courses][0]
    course = Course.objects.get(slug=slug)

    if not course:
        return HttpResponseNotFound(content="curso no encontrado")

    return render(request, 'courses/course-detail.html', {
        "course": course
    })


def course_lessons(request, id):
    lesson = {
        "course_title": "Django aplicaciones",
        "progress": 30,

        "course_content": [
            {
                "id": 1,
                "name": "Introduccion al curso",
                "total_lessons": 6,
                "complete_lessons": 3,
                "lessons": [
                        {
                            "name": "¿Que obtentdrás de este curso?",
                            "type": "video"
                        },
                    {
                            "name": "¿Como usar la plataforma?",
                            "type": "article"
                        },
                ]
            }
        ]
    }

    return render(request, 'courses/course-lessons.html', {
        "lesson": lesson
    })
