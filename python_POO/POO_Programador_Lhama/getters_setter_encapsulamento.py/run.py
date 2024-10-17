class MinhaClasse:
    def __init__(self):
        self.__valor = None
        self._elem = None

    def setter(self, valor: int) -> None:
        self.__valor = valor    
        
    def getter(self) -> int:
        return self.__valor    

minha_classe = MinhaClasse()
# minha_classe.__valor = 4 # Ferindo o encapsulamento
# print(minha_classe.__valor)
print(minha_classe.setter(10)) # Saída: None
print(minha_classe.getter()) # Saída: 10