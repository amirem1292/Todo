from django.contrib import admin
from .models import *
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    search_fields = ('title', )
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('info', {'fields': ('author', 'title', 'is_done')}),
        ('date', {'fields': ('created_at', 'updated_at')}),
    )
    add_fieldsets = (
        ('info', {'fields': ('author', 'title', 'is_done')}),
    )

admin.site.register(Task, TaskAdmin)