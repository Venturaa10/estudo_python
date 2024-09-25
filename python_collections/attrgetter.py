from operator import attrgetter

# Testando "attrgetter"
# Utilizado para acessar de forma eficiente atributos de objetos
# "attrgetter" especifica que a ordenação deve ser feita com base no atributo X ("_numero" nesse caso) de cada objeto
class Conta:
    def __init__(self, numero, saldo):
        self._numero = numero
        self._saldo = saldo

    def __repr__(self):
        return f'Conta(numero={self._numero}, saldo={self._saldo})'

contas2 = [Conta(123, 1000), Conta(456, 500), Conta(789, 1500)]

# Ordena as contas pelo saldo
for conta in sorted(contas2, key=attrgetter('_numero')):
    print(conta)
