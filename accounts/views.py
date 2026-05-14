from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Formulário pronto do django para criação de usuários.
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def register_view(request):
     if request.method == 'POST':
          user_form = UserCreationForm(request.POST)
          if user_form.is_valid():
               user_form.save()
               return redirect('login')  
               # Redireciona para a página de login após o registro bem-sucedido. 
     else:
          user_form = UserCreationForm()
     return render(request, 'register.html', {'user_form': user_form})

def login_view(request):
     if request.method == 'POST':

          user_name = request.POST.get('username')
          password = request.POST.get('password')
          user = authenticate(request, username=user_name, password=password)
           # Verifica se o usuário e a senha estão cadastrados no banco de dados.

          if user is not None:
               login(request, user)
               return redirect('cars_list')
               # Redireciona para a página principal após o login bem-sucedido.
          else:
               login_form = AuthenticationForm()
         
     else:
          login_form = AuthenticationForm()
     return render(request, 'login.html', {'login_form': login_form})

def logout_view(request):
     logout(request)
     return redirect('cars_list')
      