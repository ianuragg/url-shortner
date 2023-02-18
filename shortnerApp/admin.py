from django.contrib import admin
from . models import Shortner

# Shortner model
@admin.register(Shortner)
class ShortnerAdmin(admin.ModelAdmin):
    list_display = ('url', 'slug', 'date_created', 'is_active')
    ordering = ('slug',)
    search_fields = ('slug',)
