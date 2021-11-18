import random
import string


"'criar random password para os usuários'"
def criarRandomPassword():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(8))
    return password

def criarCodigoResgate():
    characters = '#' + string.ascii_lowercase + string.digits
    codigo = ''.join(random.choice(characters) for i in range(5))
    return codigo