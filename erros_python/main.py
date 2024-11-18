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
        # É uma boa pratica criar todos os atributos da classe, dentro de seu inicializador.
        self.__saldo = 100
        self.cliente = cliente        
        self.__set_agencia(agencia) # Verifica valor de agencia atraves do setter.
        self.__numero = numero
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

    @property
    def agencia(self):
        return self.__agencia
    
    def __set_agencia(self, value): 
        ''' Metodo setter privado para o atributo "agencia", responsavel por realizar as verificações necessarias antes de atribuir um valor ao mesmo'''
        if not isinstance(value, int):
            return
        if value <= 0:
            print('O atributo agencia deve ser maior que zero')
            return
        
        self.__agencia = value

    @property
    def numero(self):
        return self.__numero
    
    def __set_numero(self, value):
        if not isinstance(value, int):
            return
        if value <= 0:
            return
        
        self.__numero = value

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, int):
            return
        if value <= 0:
            return
        self.__saldo = value

    def transferir(self, valor, favorecido):
        favorecido.depositar(valor)

    def sacar(self, valor):
        self.saldo += valor

    def depositar(self, valor):
        self.saldo += valor


conta_corrente1 = ContaCorrente(None, 'agencia falsa', '22500')
conta_corrente1.agencia = 0
print(conta_corrente1.agencia)

cliente1 = Cliente('João Victor', '11122233345', 'Engenheiro de Software')
cliente1.idade = 20
print(f'\n{cliente1.idade}')
pprint(cliente1.__dict__, width=40) # Os atributos do objeto são exibidos na sixtaxe de um dicionario.

