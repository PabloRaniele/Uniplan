# from django import forms
# from .models import Perfil

# class PerfilForm(forms.ModelForm):
#     class Meta:
#         model = Perfil
#         fields = ['cpf', 'endereco', 'sexo', 'tel', 'nasc', 'avatar']
#         widgets = {
#             'cpf': forms.TextInput(attrs={'placeholder': 'CPF'}),
#             'endereco': forms.TextInput(attrs={'placeholder': 'Endereço'}),
#             'sexo': forms.Select(attrs={'placeholder': 'Sexo'}),
#             'tel': forms.TextInput(attrs={'placeholder': 'Telefone'}),
#             'nasc': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Data de Nascimento'}),
#             'avatar': forms.ClearableFileInput(attrs={'placeholder': 'Avatar'}),
#         }
