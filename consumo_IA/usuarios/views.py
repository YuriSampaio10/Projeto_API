from django.shortcuts import render, redirect #render= renderiza as paginas html; redirect= redireciona
from django.http import HttpResponse #função para retornar uma resposta http pro usuario

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
           

        return HttpResponse (f'{username}')