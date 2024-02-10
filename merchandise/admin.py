from django.contrib import admin

from merchandise.models import Merchandise


@admin.register(Merchandise)
class MerchandiseAdmin(admin.ModelAdmin):
    pass
