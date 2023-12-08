from django.contrib import admin
from .models import Todo, Tag

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'timestamp')
    list_filter = ('status',)
    search_fields = ('title', 'description')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Todo, TodoAdmin)
admin.site.register(Tag, TagAdmin)
