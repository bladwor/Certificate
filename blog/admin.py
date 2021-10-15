from django.contrib import admin
from django import forms
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    list_display = (
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
    form = PostAdminForm


admin.site.register(Post, PostAdmin)
