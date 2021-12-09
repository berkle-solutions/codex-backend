from django.core.mail import send_mail
from django.shortcuts import render
#from django.http import JsonResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf import settings
#from django.http import HttpResponse

# def enviar_email_cadastro(email, senha):
#     try: 
#         send_mail(
#             'Seu acesso ao Codex - gestão de encomendas',
#             'Seus dados de usuário e senha:\n'+'usuário: ' + email + '\n' + 'senha: ' + senha + '\nPara notificar suas encomendas, é obrigatório a validação via whatsapp\nPor favor, clique neste link https://api.whatsapp.com/send/?phone=447860099299&text=JULIOVAZ&app_absent=0, e envie a mensagem\n',
#             'noreply@codex.com.br',
#             [email]
#         )
#     except Exception as e:
#         raise e


def enviar_email_cadastro(email, senha):
    try:
            html_tpl_path = 'email_templates/welcome.html'
            context_data = {'name': 'Morador'}
            email_html_template = get_template(html_tpl_path).render(context_data)
            receiver_email = 'jorgefaria.barcelos+1@gmail.com'
            email_msg = EmailMessage('Bem vindo ao Codex',
            email_html_template, settings. APPLICATION_EMAIL,
            [receiver_email],
            reply_to=[settings.APPLICATION_EMAIL]
            )
            
            email_msg.content_subtype = 'html'
            email_msg.send(fail_silently=False)

    except Exception as e:
        raise e