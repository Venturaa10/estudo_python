class MinhaClasse:
    estatico = 'João Victor' # Variavel Estatica 

    def __init__(self, estado) -> None:
        self.estado = estado

    def print_variavel_de_classe(self):
        print(self.estatico)

    @classmethod
    def alteracao_da_variavel_de_classe(cls):
        # Resumido: MinhaClasse.estatico = 'Alterando...'
        cls.estatico = 'Alterando...'



objeto_01 = MinhaClasse(True)
objeto_02 = MinhaClasse(True)

print(objeto_01.estatico) # João Victor
print(objeto_02.estatico) # João Victor
print(MinhaClasse.estatico) # João Victor

objeto_01.alteracao_da_variavel_de_classe() # A alteração é aplicada para todos os objetos, não apenas para o objeto_01
print(objeto_01.estatico) # Alterando...
print(objeto_02.estatico) # Alterando...
print(MinhaClasse.estatico) # Alterando...

