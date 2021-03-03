import random


class Conta:
    __contas = dict()

    def __init__(self, nome):
        self._nome = nome
        self._conta = self.__geradorNumero(nome)

    def __str__(self):
        return f'Nome: {self._nome} -- Conta: {self._conta} -- Saldo: R${Conta.__contas[self._nome][self._conta]:.02f}'


    def __geradorNumero(self, nome):
        if nome not in Conta.__contas:
            Conta.__contas[nome] = dict()

        while True:
            numero_gerado = random.randint(1, 999)
            for key, valueDict in Conta.__contas.items():
                if key == nome and valueDict != numero_gerado:
                    Conta.__contas[nome][numero_gerado] = self._value = 0
            break
        return numero_gerado

    @staticmethod
    def contas_do_usuario(nome):
        if nome in Conta.__contas:
            listaTemporaria = list()
            for key in Conta.__contas[nome].keys():
                listaTemporaria.append(key)
            print(f'Listas de contas do usuário {nome}: {listaTemporaria}')
        else:
            print(f'{nome} não possui contas')

    def deposito(self, nome, conta, valor):
        Conta.__contas[nome][conta] += valor

    def saque(self, nome, conta, valor):
        if Conta.__contas[nome][conta] >= valor:
            Conta.__contas[nome][conta] -= valor
        else:
            print('Saldo insuficiente')

    def transferencia(self, nome, conta, valor, contaDest):
        if Conta.__contas[nome][conta] >= valor:
            self.saque(valor)
            contaDest.deposito(valor)
            print('Transferência realizada com sucesso')
        else:
            print('Transferência não realizada: Saldo insuficiente')