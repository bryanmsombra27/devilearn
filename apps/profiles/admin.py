from django.contrib import admin
from .models import InstructorProfile, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + \
        (("Rol personalizado", {"fields": ("is_instructor",)}),)
    add_fieldsets = BaseUserAdmin.add_fieldsets + \
        ((None, {"fields": ("is_instructor",)}),)


# Register your models here.
admin.site.register(InstructorProfile)
