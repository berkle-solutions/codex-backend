from django.urls import path
from codex.views.localizacao_view import LocalizacaoView
from codex.views.autenticacao_view import AutenticacaoView
from codex.views.encomenda_view import EncomendaView
from codex.views.armario_view import ArmarioView
from codex.views.pessoa_view import PessoaView
from codex.views.perfil_view import PerfilView
from codex.views.compartimento_view import CompartimentoView
from codex.views.notificacao_view import NotificacaoView


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
    path('pessoa/enviar/pin', PessoaView.enviar_pin_2fa, name="enviar-pin-2fa"),
    path('pessoa/verificar/pin', PessoaView.verificar_pin_2fa, name="verificar-pin-2fa"),
    path('pessoa/verificar/pin/resend', PessoaView.reenviar_pin_2fa, name="reenvier-verificar-pin-2fa"),
    #encomenda
    path('encomenda/salvar', EncomendaView.salvar_encomenda, name="salvar-encomenda"),
    path('encomenda/lista', EncomendaView.retorna_encomenda, name="retorna-encomendas"),
    path('encomenda/detalhe/<str:pk>', EncomendaView.detalhe_encomenda, name="detalhe-encomenda"),
    path('encomenda/deletar/<str:pk>', EncomendaView.deletar_encomenda, name="deletar-encomenda"),
    path('encomenda/atualizar', EncomendaView.atualizar_encomenda, name="atualizar-encomenda"),
    path('encomenda/estoque', EncomendaView.registrar_encomenda_estoque, name="atualiza-encomenda-estoque"),
    path('encomenda/resgate', EncomendaView.resgatar_encomenda, name="resgatar-encomenda"),
    #autenticacao
    path('autenticacao/token', AutenticacaoView.autenticar_usuario, name="autenticacao"),
    # path('autenticacao/token', TokenObtainPairView.as_view(), name="autenticacao-token"),
    # path('autenticacao/token/refresh/', TokenRefreshView.as_view(), name='autenticacao-token-refresh'),
    # armario
    path('armario/lista', ArmarioView.retorna_armarios, name="retorna-armarios"),
    path('armario/detalhe/<str:pk>', ArmarioView.detalhe_armario, name='detalhe-armario'),
    path('armario/salvar', ArmarioView.salvar_armario, name='salvar-armario'),
    path('armario/atualizar/<str:pk>', ArmarioView.atualizar_armario, name='atualizar-armario'),
    path('armario/deletar/<str:pk>', ArmarioView.deletar_armario, name='deletar-armario'), 
    # compartimento
    path('compartimento/lista-por-armario/<str:armario_id>', CompartimentoView.retorna_compartimentos_por_armario, name="retorna-compartimentos-por-armario"),
    path('compartimento/detalhe/<str:pk>', CompartimentoView.detalhe_compartimento, name='detalhe-compartimento'),
    path('compartimento/salvar', CompartimentoView.salvar_compartimento, name='salvar-compartimento'),
    path('compartimento/atualizar/<str:pk>', CompartimentoView.atualizar_compartimento, name='atualizar-compartimento'),
    path('compartimento/deletar/<str:pk>', CompartimentoView.deletar_compartimento, name='deletar-compartimento'),
    # localizacao
    path('localizacao/lista', PessoaView.buscar_pessoas_por_andar_bloco, name='buscar-localizacao'),
    #notificacao
    path('notificacao/enviar', NotificacaoView.enviar_notificacao, name="enviar-notificacao"),
    #path('sendemail/', send_email_api),
]
