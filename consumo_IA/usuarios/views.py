from django.shortcuts import render, redirect #render= renderiza as paginas html; redirect= redireciona
from django.http import HttpResponse #função para retornar uma resposta http pro usuario
from django.contrib.auth.models import User #tabela do banco de dados 
from django.contrib.messages import constants #tipo de erro
from django.contrib import messages #função que cria a msg

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
            messages.add_message(request, constants.ERROR, "As senhas devem ser iguais")
            return redirect('cadastro')
        
        #verifica se a senha tem menos de 6 digitos
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, "As senhas devem ter mais de 6 digitos")
            return redirect('cadastro')
        
        #verifica no db se tem usuarios com o username escolhido
        user = User.objects.filter(username=username)

        #exibe a mensagem caso ja exista um usuario em o username digitado
        if user.exists():
            messages.add_message(request, constants.ERROR, "Já existe um usuário com esse username")
            return redirect('cadastro')
        
        #verifica no db se tem usuarios com o username escolhido
        email = User.objects.filter(email=email)

        #exibe a mensagem caso ja exista um usuario em o email digitado
        if email.exists():
            messages.add_message(request, constants.ERROR, "Já existe um usuário com esse email")
            return redirect('cadastro')

        #armazena o que foi digitado em uma tabela no db
        user = User.objects.create_user(
            username=username,
            email=email,
            password=senha
        )
           

        return redirect('login')
    

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')