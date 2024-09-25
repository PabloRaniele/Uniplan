from django.db import models
 
class Funcionario(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=15)
    endereco = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1)
    tel = models.CharField(max_length=15)
    nasc = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.nome
 
class Veterinario(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE,
                                    related_name='Veterinario')
    doutor = models.CharField(max_length=40)
    crmv = models.CharField(max_length=30)  #Exemplo: CRMV-SP 12345
   
    def __str__(self):
        return self.doutor

    
class Tutor(models.Model):
    tutor_nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=15)
    tel = models.CharField(max_length=15)
    ender = models.CharField(max_length=15)
   
    def __str__(self):
        return self.tutor_nome

class Animal(models.Model):
    Animal_choices = [
        ('gato', 'Gato'),
        ('cachorro', 'Cachorro'),
        ('aves', 'Aves'),
    ]
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE,
                                 related_name='Animal')
    nome_pet = models.CharField(max_length=30, null=True, blank=True)
    peso_pet = models.FloatField(max_length=30)
    idade_pet = models.CharField(max_length=2, null=True, blank=True)
    raca_pet = models.CharField(max_length=30, null=True, blank=True)
    tipo = models.CharField(max_length=30, choices=Animal_choices, default='gato')
    
    def __str__(self):
        return f'{self.nome_pet} ({self.get_tipo_display()})'
        

class Sintomas(models.Model):
    Sintomas_choices = [
        ('verde', 'Verde'),
        ('amarelo', 'Amarelo'),
        ('vermelho', 'Vermelho'),
    ]
    sintomas = models.CharField(max_length=14, null=True, blank=True)
    grau_sint = models.CharField(max_length=30, choices=Sintomas_choices, default='verde')
    descricao = models.CharField(max_length=30)
    
    def __str__(self):
        return self.sintomas
    
class Consulta(models.Model):
    Sintomas_choices = [
        ('verde', 'Verde'),
        ('amarelo', 'Amarelo'),
        ('vermelho', 'Vermelho'),
    ]
    sintomas = models.ForeignKey(Sintomas, on_delete=models.CASCADE,
                                 null=True, related_name='Consulta')
    nome_proced = models.CharField(max_length=30, default=True)
    duracao = models.TimeField(max_length=30, null=True, blank=True)
    
    grau_de_risco = models.CharField(max_length=30, null=True, blank=True,choices=Sintomas_choices, default='verde')
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome_proced

class Loja(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE,
                                    related_name='Loja')
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE,
                                    related_name='Loja')              
    nome_loja = models.CharField(max_length=100)  
    endereco = models.CharField(max_length=200)  
    telefone = models.CharField(max_length=20)  
    email = models.EmailField()  

    def __str__(self):
        return self.nome_loja
    
class Agendamento(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE) 
    nome_agend = models.CharField(max_length=30, null=True, blank=True)
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)          
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)                                                  
    data_agend = models.DateTimeField(null=True, blank=True)
     
    def __str__(self):
        return self.nome_agend


