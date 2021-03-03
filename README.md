# Exercício
Implemente um sistema para bancos com os requisitos a seguir:

 - Existem 2 tipos de contas: conta corrente e conta poupança
 - Para criar uma conta deve ser utilizado apenas o nome do usuário
	 - O número da conta deve ser gerado aleatoriamente (utilize método apresentado abaixo) e inserido em um dicionario protegido
	 - Cada número da conta deve ser único
	 - Um método estático deve retornar uma lista de contas a partir de um nome
 - Toda conta deve conter os métodos **saque**, **deposito** e **transferencia**
	 - Apenas uma conta do tipo conta corrente pode fazer transferência pra qualquer outra conta
		 - Parâmetros para transferência: conta e valor
 - Uma conta poupança não pode ficar com saldo negativo
 - Uma conta poupança tem o método **rende**, que aplica a taxa de 0.95% sobre o saldo da poupança
 - Todo saque em uma conta poupança tem uma taxa de R$2
 - Nenhum saque pode ser maior que o valor existente em conta


 **if** __ name __ == "__ **main** __":
 
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
