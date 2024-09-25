from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

def sintomas_view(request):
    return render(request, 'sintomas.html')

def atend_view(request):
    return render(request, 'atend.html')

def cadastro_pet_view(request):
    return render(request, 'CadastroPet.html')

def cadastro_funcio_view(request):
    return render(request, 'CadFuncio.html')

def home_view(request):
    return render(request, 'home.html')