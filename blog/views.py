from django.shortcuts import redirect, render, HttpResponse
from django.views import View

from .models import Post
from blog.service import error_404

from moduls.sqlserver import SQLserver
from moduls.examination import Examination


class Blog_page(View):
    '''Отрисовка главной страницы'''

    @staticmethod
    def get(request):
        try:
            posts = Post.objects.filter(status='published')
        except Post.DoesNotExist:
            return error_404(request)

        context = {
            'posts': posts,
        }

        return render(request, 'blog/index.html', context)


class Certificat_page(View):
    '''Отрисока сертификата и резервирование его кода из БД'''

    @staticmethod
    def get(request, id, *args, **kwargs):
        try:
            post = Post.objects.get(status='published', pk=id)
        except Post.DoesNotExist:
            return error_404(request)

        posts = Post.objects.filter(status='published')

        '''вытаскиваем свободный код из БД'''
        code = SQLserver.code_certificat()

        context = {
            'posts': posts,
            'post': post,
            'code': code[0]['card_code'],
        }

        return render(request, 'blog/certificat.html', context)


class Politic_page(View):
    '''Редирект на файл с политикой пользовательского соглашения'''

    @staticmethod
    def get():
        return redirect('/static/pol_isp.pdf')


class Success_page(View):
    '''Страница если оплата прошла успешно'''

    @staticmethod
    def get(request):
        posts = Post.objects.filter(status='published')
        context = {
            'posts': posts,
        }

        '''Проверка платежей'''
        Examination.update_status()
        return render(request, 'blog/success.html', context)


class Failed_page(View):
    '''Страницы об ошибке при оплате'''

    @staticmethod
    def get(request):
        posts = Post.objects.filter(status='published')
        context = {
            'posts': posts,
        }

        Examination.update_status()
        return render(request, 'blog/failed.html', context)


class Examination_code(View):
    '''
        Страница куда сервис екваиринга шлет уведомления по платежам
        Так же скрипт cronexam.py из cron по таймингу шлет get запрос на проверку платежей
    '''

    @staticmethod
    def get():
        Examination.update_status()
        return HttpResponse('test')


class Email(View):
    '''
        Отрисовка шаблона emeal письма, 
        что получает пользователь при успешной оплате
    '''

    @staticmethod
    def get(request, *args, **kwargs):
        return render(request, 'blog/email2.html')
