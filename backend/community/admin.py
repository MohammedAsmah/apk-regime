from django.contrib import admin
from .models import Post, Challenge

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'content_preview', 'likes_count', 'created_at')
    search_fields = ('user__username', 'content')

    def content_preview(self, obj):
        return obj.content[:50]

@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'participants_count')
    search_fields = ('title', 'description')

    def participants_count(self, obj):
        return obj.participants.count()