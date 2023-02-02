from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import *

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cat', 'time_created', 'get_html_photo', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_editable = ('is_published', 'cat')
    list_filter = ('is_published', 'time_created')
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'content', 'photo', 'get_html_photo', 'is_published', 'cat', 'time_created', 'time_updated')
    readonly_fields = ('time_created', 'time_updated', 'get_html_photo')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=40 height=50>")

    get_html_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Админ-панель сайта'
admin.site.site_header = 'Админ-панель сайта'