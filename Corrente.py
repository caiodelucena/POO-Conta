from Conta import Conta

class Corrente(Conta):
    def __init__(self, nome):
        super().__init__(nome)

    def deposito(self, valor):
        super().deposito(self._nome, self._conta, valor)

    def saque(self, valor):
        super().saque(self._nome, self._conta, valor)

    def transferencia(self, valor, contaDest):
        super().transferencia(self._nome, self._conta, valor, contaDest)