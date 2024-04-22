from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image

from adminsortable2.admin import SortableAdminMixin, SortableStackedInline


MAX_WIDTH = 200
MAX_HEIGHT = 200


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    autocomplete_fields = ['place']


class ImageInline(SortableStackedInline):
    model = Image

    readonly_fields = ['get_preview']
    fields = ['place', 'image', 'get_preview', 'number']

    def get_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width: {}px; max-height: {}px;" />',
                obj.image.url, MAX_WIDTH, MAX_HEIGHT)

        return format_html(
            '<span style="color:red;">Error: Image not found</span>')


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    search_fields = ['title']

    inlines = [
        ImageInline,
    ]
