import random
import string


"'criar random password para os usuários'"
def criarRandomPassword():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(8))
    return password