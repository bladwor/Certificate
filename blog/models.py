from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    '''Модель сертификатов в виде постов'''
    
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )


    title = models.CharField(max_length=250)
    price = models.CharField(max_length=10, blank = True)
    image = models.ImageField(upload_to="img/thumbnail/", )
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')


    class Meta:
        ordering = ('slug',)


    def __str__(self):
        return self.title
