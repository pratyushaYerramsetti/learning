from django.contrib import admin

# Register your models here.
from .import models
# Register your models here.

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'author', ]
    list_filter = ['branch', ]
    search_fields = ['title', ]
