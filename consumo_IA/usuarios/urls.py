from django.urls import path #função que cria urls
from . import views #import o arquivo views 
from django.urls import path, include #include = adiciona uma url em outra

urlpatterns = [
    path('cadastro/' , views.cadastro , name='cadastro'),
    path('login/' , views.login , name='login'),
    path('api/' , include ('api.urls')),
]
