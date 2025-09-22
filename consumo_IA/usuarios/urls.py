from django.urls import path #função que cria urls
from . import views #import o arquivo viewa 

urlpatterns = [
    path('cadastro/' , views.cadastro , name='cadastro'),
    path('login/' , views.login , name='login'),
]
