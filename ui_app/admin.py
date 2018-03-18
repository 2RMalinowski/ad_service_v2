from django.contrib import admin
from .models import Answer, TempPost


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(Answer, AnswerAdmin)


class TempPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(TempPost, TempPostAdmin)



