from django.contrib import admin

from member.models import Credit, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ("username", "email", "last_name", "first_name", "is_active", )
    readonly_fields = ("username", "email", "last_name", "first_name", )


@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ("user__username", "balance", )
    fields = ("user", "balance", )
    readonly_fields = ("user", )

    def user__username(self, obj):
        return obj.user.username
    user__username.short_description = 'Username'
