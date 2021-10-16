from django.shortcuts import redirect, render, HttpResponse
from django.views import View

from .models import Post
from blog.service import error_404

from modules.sqlserver import SQLserver
from modules.examination import Examination


class Blog_page(View):
    '''Главная страница'''

    @staticmethod
    def get(request):
        '''Вывод всех опубликованных сертификатов'''
        
        try:
            posts = Post.objects.filter(status='published')
        except Post.DoesNotExist:
            return error_404(request)

        context = {
            'posts': posts,
        }

        return render(request, 'blog/index.html', context)


class Certificat_page(View):
    '''Страница сертификата'''

    @staticmethod
    def get(request, id):
        '''Вывод сертификата и присвоение в форму оплаты название и резервирование номера'''

        try:
            post = Post.objects.get(status='published', pk=id)
        except Post.DoesNotExist:
            return error_404(request)

        posts = Post.objects.filter(status='published')

        '''Получаем номер свободного сертификата и резервируем его для пользователя'''
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
    '''Оплата прошла успешно'''

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
    '''Ошибка при оплате'''

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
        Получение уведомлений от платежной системы после транзакции
    '''

    @staticmethod
    def get():
        Examination.update_status()
        return HttpResponse('test')


class Email(View):
    '''
        Email шаблон пользовательского письма
        для внутреннего использования
    '''

    @staticmethod
    def get(request):
        return render(request, 'blog/email2.html')
