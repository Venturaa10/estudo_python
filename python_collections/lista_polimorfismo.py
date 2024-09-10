class Conta:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'Código: {self._codigo} | Saldo {self._saldo}'
    
# Classes filhas que herdam da classe Conta
class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

# Conta Conta Corrente
conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()

# Conta Conta Poupança
conta20 = ContaPoupanca(20)
conta20.deposita(1000)
conta20.passa_o_mes()

contas = [conta16, conta20]

for conta in contas:
    print(conta)