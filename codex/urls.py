from django.urls import path

from codex.views.pessoa_view import PessoaView
from codex.views.perfil_view import PerfilView


urlpatterns = [
    # TODO: to create api overview, sounds like a swagger
	# path('', views.apiOverview, name="api-overview"),
    #perfil
	path('perfil/salvar', PerfilView.salvar_perfil, name="salvar-perfil"),
    path('perfil/detalhe/<str:pk>', PerfilView.detalhe_perfil, name="detalhe-perfil"),
    path('perfil/atualizar', PerfilView.atualizar_perfil, name="atualizar-perfil"),
    path('perfil/deletar/<str:pk>', PerfilView.deletar_perfil, name="deletar-perfil"),
    path('perfil/lista', PerfilView.retorna_perfis, name="retorna-perfis"),
    #pessoa
    path('pessoa/salvar', PessoaView.salvar_pessoa, name="salvar-pessoa")
]
