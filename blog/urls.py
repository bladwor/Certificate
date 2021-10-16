from django.urls import path
from . import views
from .views import Blog_page, Certificat_page, Success_page, Failed_page, Examination_code, Politic_page, Email

urlpatterns = [
    path('', Blog_page.as_view(), name='home'),
    path('certificat/<int:id>/', Certificat_page.as_view(), name='certificat'),
    path('success/', Success_page.as_view(), name='success'),
    path('failed/', Failed_page.as_view(), name='failed'),
    path('examination/', Examination_code.as_view(), name='examination'),
    path('politic/', Politic_page.as_view(), name='politic'),
    
    # шаблон электронного письма для внутреннего использования
    # path('email/', Email.as_view(), name='email'),
]
