from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import InstructorProfile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_instructor_profile(sender, instance, created, **kwargs):
    if created and instance.is_instructor:
        InstructorProfile.objects.create(user=instance)
