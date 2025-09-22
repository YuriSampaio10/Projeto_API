from django.shortcuts import render, redirect #render= renderiza as paginas html; redirect= redireciona
from django.http import HttpResponse #função para retornar uma resposta http pro usuario
from django.contrib.auth.models import User #tabela do banco de dados 

# Create your views here.

def cadastro(request): 
    if request.method == "GET": #metodo get ao acessar pelo navegador
        return render(request, 'cadastro.html')
    elif request.method == "POST": #metodo post é requisição do formulario html

        #armazena o que foi digitado em variaveis
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

        #verifica se as senhas são iguais
        if senha != confirmar_senha:
            print("ERRO 2")
            return redirect('cadastro')
        
        #verifica se a senha tem menos de 6 digitos
        if len(senha) < 6:
            return redirect('cadastro')
        
        #verifica no db se tem usuarios com o username escolhido
        user = User.objects.filter(username=username)

        if user.exists():
            return redirect('cadastro')

        #armazena o que foi digitado em uma tabela no db
        user = User.objects.create_user(
            username=username,
            email=email,
            password=senha
        )
           

        return HttpResponse (f'{username}')