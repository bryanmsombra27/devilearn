from django.db import models
from django.conf import settings
from .course import Course


class Progress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    progress = models.FloatField(default=0.0)

    class Meta:
        unique_together = ("user", "course")

    def __str__(self):

        return f""" {self.user.username}  - {self.course.title}: {self.progress} """
