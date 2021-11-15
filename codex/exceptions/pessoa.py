
class PessoaException:
    def __init__(self):
        self.EMAIL_ALREADY_IN_USE = 'E-mail já está em uso.'
        self.INVALID_FIELDS = 'Erro ao efetuar cadastro, dados inválidos.'

def pessoaExceptions():
    return PessoaException()