class MinhaClasse:
    def __init__(self):
        self.__valor = None
        self._elem = None

    def setter(self, valor: int) -> None:
        self.__valor = valor    

    @property        
    def getter(self) -> int:
        return self.__valor    

minha_classe = MinhaClasse()
print(minha_classe.getter)