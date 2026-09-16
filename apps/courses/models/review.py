from django.db import models
from django.conf import settings
from .course import Course


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "course")

    def __str__(self):

        return f""" {self.user.username} - {self.course.title} comento {self.comment} y califico el curso:{self.rating}   """
