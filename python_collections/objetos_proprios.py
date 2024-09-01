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
print(contas[0], contas[1])

# Vai pegar a conta_joao (representada pelo indice 0) e depositar 500 reais
print('Deposito de +500')
contas[0].deposita(500) 

print(contas[0], contas[1])

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(150)

print('Deposito de +150')
deposita_para_todas(contas)
print(contas[0], contas[1])

