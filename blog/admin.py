from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'publish',
        'price',
        'status'
    )
    list_filter = (
        'status',
        'created',
        'publish'
    )
    search_fields = (
        'title',
        'body'
    )


admin.site.register(Post, PostAdmin)
