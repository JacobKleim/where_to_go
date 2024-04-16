from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


class ImageInline(admin.TabularInline):
    model = Image

    readonly_fields = ['get_preview']
    fields = ['place', 'image', 'get_preview', 'number']

    def get_preview(self, obj):
        try:
            return format_html(
                '<img src="{}" style="max-width: 200px; max-height: 200px;" />'
                .format(obj.image.url))
        except Exception as e:
            return format_html(
                '<span style="color:red;">Error: {}</span>'.format(str(e)))


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):

    inlines = [
        ImageInline,
    ]
