from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import CadastroForm
from django.db import connection
from django.contrib import messages


#rota da página inicial

def index(request):
    return render(request, 'homepage/index.html')

def okIndex(request):
    return render(request, 'logado/okIndex.html')

#rota da página de login

def logIndex(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        senha = request.POST['password']

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM appHomepage_cadastro WHERE usuario = %s AND senha = %s", [usuario, senha])
            row = cursor.fetchone()

        if row is not None:
            # Autenticação bem-sucedida
            response_data = {'success': True, 'user': usuario}  
            return JsonResponse(response_data)  
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return JsonResponse({'success': False}) 
    return render(request, 'login/logIndex.html')

#rota da página de cadastro

def cadIndex(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url-log') # Redirecione para uma página de sucesso ou qualquer outra página
    else:
        form = CadastroForm()
    return render(request, 'cadastro/cadIndex.html', {'form': form})


def classIndex(request):
    return render(request, 'classe/classeIndex.html')