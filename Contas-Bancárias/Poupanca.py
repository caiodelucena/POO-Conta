from Conta import Conta


class Poupanca(Conta):
    def __init__(self, nome):
        super().__init__(nome)

    def deposito(self, valor):
        valor += self.rende(valor)
        super().deposito(self._nome, self._conta, valor)

    def rende(self, valor):
        return (valor * 0.0095)

    def saque(self, valor):
        self.valor = valor+2
        super().saque(self._nome, self._conta, self.valor)

    def transferencia(self, valor, contaDest):
        print('Conta poupança não pode fazer transferências')
