import random
import string


"'criar random password para os usuários'"
def criar_random_password():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(8))
    return password

def criar_codigo_resgate():
    characters = '#' + string.ascii_lowercase + string.digits
    codigo = ''.join(random.choice(characters) for i in range(5))
    return codigo