import os
os.system('cls')

class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0
        
    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f'Codigo: {self.codigo} | Saldo: {self.saldo}\n'
    
conta_joao = ContaCorrente(10)
conta_joao.deposita(5483)

conta_vinicius = ContaCorrente(7)
conta_vinicius.deposita(4600)

contas = [conta_joao, conta_vinicius]
print(contas[0], contas[1], contas[1])

# Vai pegar a conta_joao (representada pelo indice 0) e depositar 500 reais
print('Deposito de +500')
contas[0].deposita(500) 

print(contas[0], contas[1])
def deposita_para_todas(contas):
    for conta in contas:
        # Deposita x valor para cada conta na lista contas
        conta.deposita(150)

print('Deposito de +150')
deposita_para_todas(contas)
print(contas[0], contas[1])

# print('Apos o insert')
# contas.insert(0, 76)
# print(contas[0], contas[1], contas[2])

# Não vai ser possivel realizar o deposito, pois o indice 0 é um numero inteiro, e não um objeto, logo não possui o atributo .deposita
# deposita_para_todas(contas)
# print(contas[0], contas[1], contas[2])

# tupla
print('*****************\nTrabalhando com Tuplas')
# Segue um padrão definido por mim, sendo: nome, idade e ano
pedro = ('Pedro', 25, 1999)
leo = ('Leo', 30, 1994)

usuarios = [pedro, leo] # Criando uma lista de tuplas
print(usuarios)

usuarios.append(('Ana', 39, 1979)) # Adicionando um novo usuario a lista
print(usuarios)

print(usuarios[0]) # Exibindo a lista de tuplas, onde indice é 0

# Trabalhando com o objeto da classe e tupla
conta_joao = ContaCorrente(15)
conta_joao.deposita(500)
conta_vinicius = ContaCorrente(322)
conta_vinicius.deposita(1000)

contas = (conta_joao, conta_vinicius) # Tupla referenciando objeto
print(contas)

for conta in contas:
    print(conta)

print('*************\nAdicionando 500 reais ao objeto de indice 0 na tupla "contas"')
contas[0].deposita(500)

for conta in contas:
    print(conta)