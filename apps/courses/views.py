from django.shortcuts import render

# Create your views here.
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


def course_list(request):

    return render(request, 'courses/courses.html', {
        "courses": courses
    })


def course_detail(request, id):
    # course = [course.id == id for course in courses][0]
    course = {
        "course_title": "Django aplicaciones",
        "course_link": "course_lessons",
        "course_image": "images/curso_2.jpg",
        "info_course": {
            "lessons": 79,
            "duration": 8,
            "instructor": "Bryan Ochoa"
        },
        "course_content": [
            {
                "id": 1,
                "name": "Introduccion al curso",
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
