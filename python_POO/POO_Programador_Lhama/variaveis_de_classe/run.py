class MinhaClasse:
    estatico = 'João Victor' # Variavel Estatica 

    def __init__(self, estado) -> None:
        self.estado = estado


objeto_01 = MinhaClasse(True)
objeto_02 = MinhaClasse(True)

print(objeto_01.estatico)
print(objeto_02.estatico)

MinhaClasse.estatico = 'Ventura'
print(objeto_01.estatico)
print(objeto_02.estatico)

objeto_01.estatico = 'Novo'
MinhaClasse.estatico = 'Oliveira'
print(objeto_01.estatico)
print(objeto_02.estatico)