from pprint import pprint

class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao

class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.saldo = 100
        self.cliente = cliente
        self.agencia = agencia
        self.numero = numero
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

    def transferir(self, valor, favorecido):
        favorecido.depositar(valor)

    def sacar(self, valor):
        self.saldo += valor

    def depositar(self, valor):
        self.saldo += valor


conta_corrente1 = ContaCorrente(None, '00', '101')


cliente1 = Cliente('João Victor', '11122233345', 'Engenheiro de Software')
# print(cliente1.nome)
cliente1.idade = 20
print(cliente1.idade)
pprint(cliente1.__dict__, width=40) # Os atributos do objeto são exibidos na sixtaxe de um dicionario.

