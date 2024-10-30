from urllib import request
from django.shortcuts import redirect, render
from django.shortcuts import render, redirect
from .models import Animal, Consulta, Tutor, Veterinario
from home.models import Animal, Funcionario, Tutor

def login_view(request):
    return render(request, 'login.html')

def sintomas_view(request):
    return render(request, 'sintomas.html')

def atend_view(request):
        
    if request.method == 'POST':
        animal_id = request.POST['animal']
        veterinario_id = request.POST['veterinario']
        grau_de_risco = request.POST['grau_de_risco']
        nome_proced = request.POST['nome_proced']
        agendamento = request.POST['agendamento']
        
        try:
            animal = Animal.objects.get(id=animal_id)
        except Animal.DoesNotExist:
            return redirect('status_agendamentos')  # redirecionar para a página de erro
        
        try:
            veterinario = Veterinario.objects.get(id=veterinario_id)
        except Veterinario.DoesNotExist:
            return redirect('status_agendamentos')  # redirecionar para a página de erro

        consulta = Consulta(
            duracao=agendamento,
            nome_proced=nome_proced,
            grau_de_risco=grau_de_risco,
            veterinario=veterinario,
            animal=animal
        )
        consulta.save()
        return redirect('sintomas')
    
    # Obter todos os animais e veterinários para o contexto
    animais = Animal.objects.all()
    veterinarios = Veterinario.objects.all()
    context = {
        "animais": animais,
        "veterinarios": veterinarios
    }
    return render(request, 'atend.html', context)
            
            
            
            # Você pode querer lidar com a exceção de forma adequada, talvez com uma mensagem de erro
            # return render(request, 'atend.html', {'veterinarios': Veterinario.objects.all(), 'error': 'Tutor não encontrado.'})




def cadastro_pet_view(request):
    if request.method == 'POST':
        tutor_id = request.POST['tutor']  # Obtendo o ID do tutor
        nome_pet = request.POST['nome_pet']
        peso_pet = request.POST['peso_pet']
        idade_pet = request.POST['idade_pet']
        raca_pet = request.POST['raca_pet']
        tipo = request.POST['tipo']
        
        # Buscar o objeto Tutor correspondente ao ID
        try:
            tutor = Tutor.objects.get(id=tutor_id)
        except Tutor.DoesNotExist:
            # Você pode querer lidar com a exceção de forma adequada, talvez com uma mensagem de erro
            return render(request, 'CadastroPet.html', {'tutores': Tutor.objects.all(), 'error': 'Tutor não encontrado.'})
        
        # Criar o objeto Animal
        animal = Animal(
            tutor=tutor,  # Passando o objeto Tutor
            nome_pet=nome_pet,
            peso_pet=peso_pet,
            idade_pet=idade_pet,
            raca_pet=raca_pet,
            tipo=tipo
        )
        animal.save()
        return redirect('home')
    
    tutores = Tutor.objects.all()
    context = {
        'tutores': tutores
    }
    
    return render(request, 'CadastroPet.html', context)


def cadastro_funcio_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereco')
        sexo = request.POST.get('sexo')
        tel = request.POST.get('tel')
        nasc = request.POST.get('nasc')

        # Verifica se todos os campos estão preenchidos
        if nome and cpf and endereco and sexo and tel and nasc:
            # Cria e salva o objeto Funcionario
            funcionario = Funcionario(nome=nome, cpf=cpf, endereco=endereco, sexo=sexo, tel=tel, nasc=nasc)
            print(funcionario)
            funcionario.save()
            return redirect('home')  # Redireciona para a página inicial ou outra de sua escolha
        else:
            # Retorna uma mensagem de erro se houver campos em branco
            return render(request, 'CadFuncio.html', {'error': 'Por favor, preencha todos os campos obrigatórios.'})

    return render(request, 'CadFuncio.html')

    
def home_view(request):
    return render(request, 'home.html')

def sobrenos_view(request):
    return render(request, 'sobrenos.html')

def comentarios_view(request):
    return render(request, 'comentarios.html')


