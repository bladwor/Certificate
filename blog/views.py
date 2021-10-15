from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import View

from .models import Post
from blog.service import error_404
from moduls.sqlserver import SQLserver
from moduls.examination import Examination

class Blog_page(View):
    @staticmethod
    def get(request, *args, **kwargs):
        try:
            posts = Post.objects.filter(status = 'published')
        except Post.DoesNotExist:
            return error_404(request)

        context = {
            'posts': posts,
        }

        return render(request, 'blog/index.html', context)


class Certificat_page(View):
    @staticmethod
    def get(request, id, *args, **kwargs):
        try:
            post = Post.objects.get(status = 'published', pk = id)
        except Post.DoesNotExist:
            return error_404(request)

        code = SQLserver.code_certificat()

        context = {
            'post': post,
            'code': code[0]['card_code'],
        }

        return render(request, 'blog/certificat.html', context)

class Politic_page(View):
    @staticmethod
    def get(request, *args, **kwargs):
        return render(request, 'blog/politic.html')


class Success_page(View):
    @staticmethod
    def get(request, *args, **kwargs):
        Examination.update_status()
        return render(request, 'blog/success.html')


class Failed_page(View):
    @staticmethod
    def get(request, *args, **kwargs):
        Examination.update_status()
        return render(request, 'blog/failed.html')

class Examination_code(View):
    @staticmethod
    def get(request, *args, **kwargs):
        Examination.update_status()
        return HttpResponse('test')

class Email(View):
    @staticmethod
    def get(request, *args, **kwargs):
        return render(request, 'blog/email2.html')
