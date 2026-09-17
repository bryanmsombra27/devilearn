from django.db import models
from django.conf import settings
from .category import Category


class Course(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name="owned_courses")
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    overview = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(
        Category, through="CourseCategory", related_name="courses")
    image = models.URLField()
    level = models.CharField(max_length=50)
    rating = models.FloatField(default=0.0)
    duration = models.FloatField(default=0.0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):

        return f""" {self.title} """


class CourseCategory(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("course", "category")

    def __str__(self):

        return f""" {self.course} - {self.category} """
