from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('sintomas/', views.sintomas_view, name='sintomas'),

    path('atendimento/', views.atend_view, name='atendimento'),

    path('cadastro-pet/', views.cadastro_pet_view, name='cadastro_pet'),
    
    path('cadastro-funcionario/', views.cadastro_funcio_view, name='cadastro_funcionario'),
    path('sobrenos/', views.sobrenos_view, name='sobrenos'),
    path('comentaios/', views.comentarios_view, name='comentarios'),
]