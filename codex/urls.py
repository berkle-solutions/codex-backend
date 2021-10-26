from django.urls import path
from codex.views.armario_view import ArmarioView
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
    path('pessoa/salvar', PessoaView.salvar_pessoa, name="salvar-pessoa"),
    path('pessoa/detalhe/<str:pk>', PessoaView.detalhe_pessoa, name="detalhe-perfil"),
    path('pessoa/deletar/<str:pk>', PessoaView.deletar_pessoa, name="deletar-pessoa"),
    path('pessoa/atualizar', PessoaView.atualizar_pessoa, name="atualizar-pessoa"),
    path('pessoa/lista', PessoaView.retorna_pessoas, name="retorna-pessoas"),

    # armario
    path('armario/lista', ArmarioView.retorna_armarios, name="retorna-armarios"),
    path('armario/detalhe/<str:pk>', ArmarioView.detalhe_armario, name='detalhe-armario'),
    path('armario/salvar', ArmarioView.salvar_armario, name='salvar-armario'),
    path('armario/atualizar/<str:pk>', ArmarioView.atualizar_armario, name='atualizar-armario'),
    path('armario/deletar/<str:pk>', ArmarioView.deletar_armario, name='deletar-armario'),    
]
