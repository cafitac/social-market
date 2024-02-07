from django.contrib import admin

from member.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ("username", "email", "last_name", "first_name", "is_active", )
    readonly_fields = ("username", "email", "last_name", "first_name", )
