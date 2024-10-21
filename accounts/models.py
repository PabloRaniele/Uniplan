# from django.db import models
# from django.contrib.auth.models import User

# class Perfil(models.Model):
#     class Sexo(models.TextChoices):
#           MASCULINO = 'M', 'Masculino'
#           FEMININO = 'F', 'Feminimo'
#           OUTROS = 'O','Outros'

#     user = models.OneToOneField(
#          User, on_delete=models.CASCADE, primary_key=True
#     )
#     cpf = models.CharField(max_length=11)
#     endereco = models.CharField(max_length=100)
#     sexo = models.CharField(max_length=1, choices=Sexo.choices, default='', blank=True, null=True)
#     tel = models.CharField(max_length=19)
#     nasc = models.DateField(blank=True, null=True)
#     avatar = models.ImageField(
#          blank=True, null=True, default='', upload_to='contas/img'
#     )

#     def __str__(self):
#         return self.user.username




          
