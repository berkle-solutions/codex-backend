from django.urls import path
from codex.views.autenticacao_view import AutenticacaoView
from codex.views.encomenda_view import EncomendaView
from codex.views.pessoa_view import PessoaView
from codex.views.perfil_view import PerfilView


urlpatterns = [
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
    #encomenda
    path('encomenda/salvar', EncomendaView.salvar_encomenda, name="salvar-encomenda"),
    path('encomenda/lista', EncomendaView.retorna_encomenda, name="retorna-encomendas"),
    path('encomenda/detalhe/<str:pk>', EncomendaView.detalhe_encomenda, name="detalhe-encomenda"),
    path('encomenda/atualizar', EncomendaView.atualizar_encomenda, name="atualizar-encomenda"),
    # TODO: fix path('encomenda/deletar/<str:pk>', EncomendaView.deletar_encomenda, name="deletar-encomenda"),
    #autenticacao
    path('autenticacao/token', AutenticacaoView.autenticar_usuario, name="autenticacao")
    # path('autenticacao/token', TokenObtainPairView.as_view(), name="autenticacao-token"),
    # path('autenticacao/token/refresh/', TokenRefreshView.as_view(), name='autenticacao-token-refresh'),
]
