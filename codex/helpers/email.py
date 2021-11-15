from django.core.mail import send_mail
# from django.http import HttpResponse

def enviarEmailDeCadastro(email, senha):
    try: 
        send_mail(
            'Seu acesso ao Codex - gestão de encomendas',
            'Seus dados de usuário e senha:\n'+'usuário: ' + email + '\n' + 'senha: ' + senha,
            'noreply@codex.com.br',
            [email]
        )
    except Exception as e:
        raise e