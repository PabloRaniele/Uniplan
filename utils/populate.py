import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
import django # noqa E402
django.setup()

from faker import Faker # noqa E402
import random # noqa E402
from datetime import timedelta
from home.models import Funcionario, Veterinario, Tutor, Animal, Sintomas, Consulta, Loja, Agendamento # noqa E402


# Função para criar funcionários
def criando_funcionarios(quantidade):
    fake = Faker('pt_BR')
    for _ in range(quantidade):
        nome = fake.name()
        cpf = fake.cpf()
        endereco = fake.address()
        sexo = random.choice(['M', 'F'])
        tel = fake.phone_number()
        nasc = fake.date_of_birth()
        
        funcionario = Funcionario(
            nome=nome, 
            cpf=cpf, 
            endereco=endereco, 
            sexo=sexo, 
            tel=tel,
            nasc=nasc
        )
        funcionario.save()


# Função para criar veterinários
def criando_veterinarios(quantidade):
    funcionarios = Funcionario.objects.all()
    fake = Faker('pt_BR')
    for _ in range(quantidade):
        funcionario = random.choice(funcionarios)
        doutor = fake.name()
        crmv = f"CRMV-{fake.state_abbr()} {random.randint(1000, 9999)}"
        
        veterinario = Veterinario(
            funcionario=funcionario, 
            doutor=doutor, 
            crmv=crmv
        )
        veterinario.save()


# Função para criar tutores
def criando_tutores(quantidade):
    fake = Faker('pt_BR')
    for _ in range(quantidade):
        nome = fake.name()
        cpf = fake.cpf()
        tel = fake.phone_number()
        ender = fake.address()
        
        tutor = Tutor(
            tutor_nome=nome, 
            cpf=cpf, 
            tel=tel, 
            ender=ender
        )
        tutor.save()


# Função para criar animais
def criando_animais(quantidade):
    tutores = Tutor.objects.all()
    fake = Faker('pt_BR')
    tipos_animais = ['gato', 'cachorro', 'aves']
    
    for _ in range(quantidade):
        tutor = random.choice(tutores)
        nome_pet = fake.first_name()
        peso_pet = round(random.uniform(2.0, 20.0), 2)
        idade_pet = random.randint(1, 15)
        raca_pet = fake.word()
        tipo = random.choice(tipos_animais)
        
        animal = Animal(
            tutor=tutor, 
            nome_pet=nome_pet, 
            peso_pet=peso_pet, 
            idade_pet=idade_pet, 
            raca_pet=raca_pet, 
            tipo=tipo
        )
        animal.save()


# Função para criar sintomas
def criando_sintomas(quantidade):
    fake = Faker('pt_BR')
    cores = ['verde', 'amarelo', 'vermelho']
    for _ in range(quantidade):
        sintomas = fake.word()
        grau_sint = random.choice(cores)
        descricao = fake.text(max_nb_chars=30)
        
        sintoma = Sintomas(
            sintomas=sintomas, 
            grau_sint=grau_sint, 
            descricao=descricao
        )
        sintoma.save()


# Função para criar consultas
def criando_consultas(quantidade):
    animais = Animal.objects.all()
    veterinarios = Veterinario.objects.all()
    sintomas = Sintomas.objects.all()
    fake = Faker('pt_BR')
    
    for _ in range(quantidade):
        animal = random.choice(animais)
        veterinario = random.choice(veterinarios)
        sintoma = random.choice(sintomas)
        nome_proced = fake.word()
        duracao = fake.time()
        grau_de_risco = random.choice(['verde', 'amarelo', 'vermelho'])
        
        consulta = Consulta(
            sintomas=sintoma, 
            nome_proced=nome_proced, 
            duracao=duracao, 
            grau_de_risco=grau_de_risco,
            animal=animal, 
            veterinario=veterinario
        )
        consulta.save()


# Função para criar agendamentos
def criando_agendamentos(quantidade):
    animais = Animal.objects.all()
    consultas = Consulta.objects.all()
    veterinarios = Veterinario.objects.all()
    fake = Faker('pt_BR')
    
    for _ in range(quantidade):
        animal = random.choice(animais)
        consulta = random.choice(consultas)
        veterinario = random.choice(veterinarios)
        nome_agend = f"Consulta {animal.nome_pet}"
        data_agend = fake.date_time_this_year() + timedelta(days=random.randint(1, 30))
        
        agendamento = Agendamento(
            animal=animal, 
            nome_agend=nome_agend, 
            consulta=consulta, 
            veterinario=veterinario, 
            data_agend=data_agend
        )
        agendamento.save()


# Executando as funções para popular os dados
criando_funcionarios(20)
criando_veterinarios(10)
criando_tutores(15)
criando_animais(30)
criando_sintomas(10)
criando_consultas(25)
criando_agendamentos(20)

print('Dados populados com sucesso!')
