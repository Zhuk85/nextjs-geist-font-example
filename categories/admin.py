from django.contrib import admin
from django.utils.html import format_html
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'sticker_count')
    search_fields = ('name',)
    readonly_fields = ('sticker_count',)
    actions = ['delete_selected']

    # Removed display_image method because Category model has no image field
    # def display_image(self, obj):
    #     if obj.image:
    #         return format_html('<img src="{}" width="50" height="50" style="border-radius: 4px;" />', obj.image.url)
    #     return "-"
    # display_image.short_description = 'Изображение'

    def sticker_count(self, obj):
        return obj.sticker_set.count()
    sticker_count.short_description = 'Количество стикеров'

    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }

    fieldsets = (
        ('Основная информация', {
            'fields': ('name',)
        }),
        ('Статистика', {
            'fields': ('sticker_count',),
            'classes': ('collapse',)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('slug',)
        return self.readonly_fields

    def save_model(self, request, obj, form, change):
        if not obj.slug:  # Only set the slug if it's not already set
            from django.utils.text import slugify
            obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)
