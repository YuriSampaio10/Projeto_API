from django.shortcuts import render, redirect #render= renderiza as paginas html; redirect= redireciona
from django.http import HttpResponse #função para retornar uma resposta http pro usuario
from django.contrib.auth.models import User #tabela do banco de dados 
from django.contrib.messages import constants #tipo de erro
from django.contrib import messages #função que cria a msg
from django.contrib import auth  #módulo de autenticação do Django (login, logout, autenticação de usuários)
from django.core.validators import validate_email #função que valida se um e-mail digitado tem formato válido (ex:nome@dominio.com)
from django.core.exceptions import ValidationError #exceção lançada quando algo não passa em uma validação (ex: e-mail inválido)



# Create your views here.

#função do usuarios/cadastro/
def cadastro(request): 
    if request.method == "GET":
        return render(request, 'cadastro.html')

    elif request.method == "POST":
        # armazena o que foi digitado em variáveis
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

         # 🔹 validação de nome (somente letras e espaços)
        if not re.match(r'^[A-Za-zÀ-ÿ\s]+$', username):
            messages.add_message(request, constants.ERROR, "O nome deve conter apenas letras e espaços.")
            return redirect('cadastro')

        # 🔹 tamanho mínimo
        if len(username) < 3:
            messages.add_message(request, constants.ERROR, "O nome deve ter pelo menos 3 caracteres.")
            return redirect('cadastro')

        # 🔹 primeira letra maiúscula
        if not username[0].isupper():
            messages.add_message(request, constants.WARNING, "Por favor, comece o nome com letra maiúscula.")

        # verifica se o username já existe
        if User.objects.filter(username=username).exists():
            messages.add_message(request, constants.ERROR, "Já existe um usuário com esse username.")
            return redirect('cadastro')
        
        # valida formato do email
        try:
            validate_email(email)
        except ValidationError:
            messages.add_message(request, constants.ERROR, "E-mail inválido.")
            return redirect('cadastro')

        # verifica se o e-mail já existe
        if User.objects.filter(email=email).exists():
            messages.add_message(request, constants.ERROR, "Já existe um usuário com esse e-mail.")
            return redirect('cadastro')
        
        # verifica se as senhas são iguais
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, "As senhas devem ser iguais.")
            return redirect('cadastro')
        
        # verifica se a senha tem pelo menos 6 dígitos
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, "A senha deve ter pelo menos 6 dígitos.")
            return redirect('cadastro')
            
        # cria o usuário no banco
        user = User.objects.create_user(
            username=username,
            email=email,
            password=senha
        )

        messages.add_message(request, constants.SUCCESS, "Usuário cadastrado com sucesso!")
        return redirect('login')
    

#função do usuarios/login/
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get("senha")

        # verifica se existe no db
        user = auth.authenticate(request, username=username, password=senha)

        if user is not None:
            auth.login(request, user)
            return redirect('/usuarios/api/ia/')

        # se falhar, mostra erro e volta ao login
        messages.add_message(request, constants.ERROR, 'Usuário ou senha incorretos')
        return redirect('/usuarios/login')