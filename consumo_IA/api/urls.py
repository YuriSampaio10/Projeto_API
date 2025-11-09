from django.urls import path #função que cria urls
from . import views #import o arquivo views 

urlpatterns = [
    path('ia/' , views.ia , name='ia'),
]
