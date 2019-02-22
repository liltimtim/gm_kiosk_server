from django.contrib import admin
from .models import Kiosk
# Register your models here.


class KioskAdmin(admin.ModelAdmin):
    readonly_fields = ('join_code',)


admin.site.register(Kiosk, KioskAdmin)
