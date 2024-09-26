from abc import ABCMeta, abstractmethod
from operator import attrgetter
from functools import total_ordering


class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        ''' Metodo utilizado para ordenar ou comparar objetos de uma classe personalizada '''
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    # Um método abstrato obriga as classes filhas a implementarem o método em sua própria classe.
    @abstractmethod
    def passa_o_mes(self):
        pass

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

class ContaInvestimento(Conta):
    def passa_o_mes(self):
        pass

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        '''  Metodo de verificação de igualdade '''
        if type(outro) != ContaSalario:
            return False
        
        # Verificação realizada através do codigo e do saldo da outra classe
        # Ou seja, so retorna True, se o codigo e o saldo forem o mesmo de ambos os objetos
        return self._codigo == outro._codigo and self._saldo == outro._saldo


    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo

        return self._codigo < outro._codigo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"Código: {self._codigo} | Saldo {self._saldo}"


class ContaMultiploSalario(ContaSalario):
    pass


'''
conta30 = ContaInvestimento(7) # Vai dar error nesse momento, pois não está incluída "passa_o_mes" na sua classe

# Conta Conta Corrente
conta16 = ContaCorrente(6)
conta16.deposita(1000)
conta16.passa_o_mes()

# Conta Conta Poupança
conta20 = ContaPoupanca(5)
conta20.deposita(1000)
conta20.passa_o_mes()

# Conta Corrente e Salario
conta1 = ContaCorrente(37)
conta1.deposita(110) 
conta2 = ContaSalario(37)
print(conta1)
print(conta2)
'''


# Linhas retornando True, pois a classe ContaSalario tem um metodo de verificação de igualdade
'''
print(conta1 == conta2) 
print(conta1 in [conta2]) 
print(conta2 in [conta1]) 


contas = [conta16, conta20]

for conta in contas:
    print(conta)
'''

# Conta MultiplosSalarios
print(isinstance(ContaCorrente(37), Conta)) # True
print(isinstance(ContaCorrente(37), ContaCorrente)) # True

# Teste
conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas2 = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

print('\nTESTE COM A FUNÇÃO extrai_saldo\n')
def extrai_saldo(conta):
    '''A ordenação é baseada no saldo da conta'''
    return conta._saldo

for conta in sorted(contas2, key=extrai_saldo):
    print(conta)


'''
# Ordenando utilizando o "attrgetter"
# Ordenação baseada no saldo da conta, utilizando a função "attrgetter"
for conta in sorted(contas2, key=attrgetter('_saldo')):
    print(conta)
'''

# Está sendo suportado por causa do metodo "lt"
print(conta_da_daniela > conta_do_guilherme)

# Está sendo suportado por causa do decorador "total_ordering" na classe ContaSalario
print(conta_do_paulo >= conta_do_guilherme)
print(conta_da_daniela <= conta_do_paulo)

'''
# Primeiro criterio de ordenação: Saldo
# Segundo criterio de ordenação: Codigo
for conta in sorted(contas2, key=attrgetter('_saldo', '_codigo')):
    print(conta)
'''

# Criterio de ordenação feita no metodo "lt" da classe, então não é necessario passar o "attrgetter" nesse caso
for conta in sorted(contas2):
    print(conta)