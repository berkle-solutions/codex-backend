
class FilaStatusEnum:
    def __init__(self):
        self.TRIAGEM = 1
        self.EM_ESTOQUE = 2
        self.RETIRADO = 3
        self.EM_ATRASO = 4

def fila_status_enum():
    return FilaStatusEnum()