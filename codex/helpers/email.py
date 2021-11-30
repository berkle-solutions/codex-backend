from django.core.mail import send_mail
# from django.http import HttpResponse

def enviar_email_cadastro(email, senha):
    try: 
        send_mail(
            'Seu acesso ao Codex - gestão de encomendas',
            'Seus dados de usuário e senha:\n'+'usuário: ' + email + '\n' + 'senha: ' + senha + '\n\n',
            'Para notificar suas encomendas, é obrigatório a validação via whatsapp',
            'Por favor, clique neste link https://api.whatsapp.com/send/?phone=447860099299&text=JULIOVAZ&app_absent=0, e envie a mensagem',
            'noreply@codex.com.br',
            [email]
        )
    except Exception as e:
        raise e