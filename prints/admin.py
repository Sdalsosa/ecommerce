from django.contrib import admin
from .models import Category, Print
from django.db.models import Count

# Register your models here.


class PrintAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'id',
        'stock',
        'price',
        'image',
        'likes_count',
    )

    ordering = ('stock',)

    def likes_count(self, obj):
        return obj.likes_count
    likes_count.short_description = 'likes'
    likes_count.admin_order_field = 'likes_count'

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).annotate(
                                    likes_count=Count('likes'))


admin.site.register(Print, PrintAdmin)
admin.site.register(Category)
