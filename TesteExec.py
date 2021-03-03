from Conta import Conta
from Poupanca import Poupanca
from Corrente import Corrente

if __name__ == "__main__":
    c1 = Corrente('Mario')
    c2 = Corrente('Jose')
    c3 = Poupanca('Jose')
    Conta.contas_do_usuario('Mario')
    Conta.contas_do_usuario('Jose')
    Conta.contas_do_usuario('Pedro')
    print(c3)
    c3.deposito(812)
    c1.deposito(812)
    print(c3)
    print(c1)
    c3.saque(818)
    c1.saque(813)
    c1.saque(800)
    print(c1)
    c3.saque(817.5)
    print(c3)
    c3.transferencia(540, c1)
    c1.transferencia(4, c2)
    print(c1)
