from django.contrib import admin
from .models import Gt
# Register your models here.

class GtAdmin(admin.ModelAdmin):
    list_display = ('title', 'destination','path')

# Register your models here.

admin.site.register(Gt, GtAdmin)