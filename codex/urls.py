from django.urls import path
from . import views

from codex.views.perfil_view import PerfilView

urlpatterns = [
    # TODO: to create api overview, sounds like a swagger
	# path('', views.apiOverview, name="api-overview"),
    #perfil
	path('perfil/salvar', PerfilView.salvar_perfil, name="salvar-perfil"),
    # path('perfil/detalhe/<str:pk>', PerfilView.detalhe_perfil, name="detalhe-perfil"),
    # path('perfil/atualizar/<str:pk>', PerfilView.atualizar_perfil, name="atualizar-perfil"),
    # path('perfil/deletar/<str:pk>', PerfilView.deletar_perfil, name="deletar-perfil")
]
