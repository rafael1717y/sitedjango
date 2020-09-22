from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from pysite.aperitivos.models import Video

@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('titulo', 'slug', 'creation', 'vimeo_id')
    ordering = ('creation',)
    prepopulated_fields = {'slug':('titulo',)}