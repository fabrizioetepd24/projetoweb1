from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota, view responsável e referência
    # www.globo.com
    # path('')
    # www.globo.com/pernambuco
    # path('globo.com/pernambuco/')

    path('',views.home,name='home'),
    path('usuarios/',views.usuarios,name='listagem_usuarios')
]
