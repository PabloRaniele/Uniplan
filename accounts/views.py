# from django.shortcuts import render

# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Perfil
# from .forms import PerfilForm

# @login_required
# def criar_perfil(request):
#     if request.method == 'POST':
#         form = PerfilForm(request.POST, request.FILES)
#         if form.is_valid():
#             perfil = form.save(commit=False)
#             perfil.user = request.user
#             perfil.save()
#             return redirect('perfil_detalhes')  # Substitua 'perfil_detalhes' pela URL da página de perfil do usuário
#     else:
#         form = PerfilForm()
#     return render(request, 'perfil/criar_perfil.html', {'form': form})

# @login_required
# def editar_perfil(request):
#     perfil, created = Perfil.objects.get_or_create(user=request.user)
#     if request.method == 'POST':
#         form = PerfilForm(request.POST, request.FILES, instance=perfil)
#         if form.is_valid():
#             form.save()
#             return redirect('perfil_detalhes')  # Substitua 'perfil_detalhes' pela URL da página de perfil do usuário
#     else:
#         form = PerfilForm(instance=perfil)
#     return render(request, 'perfil/editar_perfil.html', {'form': form})
