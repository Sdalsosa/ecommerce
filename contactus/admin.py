from django.contrib import admin
from .models import ContactUs

# Register your models here


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'subject',
        'email',
        'created_at',
    )

    ordering = ('-created_at',)


admin.site.register(ContactUs, ContactUsAdmin)
