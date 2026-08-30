from django.shortcuts import render

# Create your views here.


def course_list(request):
    courses = [
        {
            "id": 1,
            "level": "principante",
            "rating": 4.8,
            "course_title": "Python fundamentos hasta los detalles",
            "instructor": "Alison Doe",
            "course_image": "images/curso_1.jpg",
            "instructor_image": "https://randomuser.me/api/portraits/women/68.jpg"
        }
    ]

    return render(request, 'courses/courses.html', {
        "courses": courses
    })


def course_detail(request, id):
    return render(request, 'courses/course-detail.html')


def course_lessons(request, id):
    return render(request, 'courses/index.html')
