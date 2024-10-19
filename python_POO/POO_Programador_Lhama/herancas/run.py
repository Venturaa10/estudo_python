class Mamifero:
# Observação: A classe Mamifero não consegue acessar os metodos das classes filhas
    def __init__(self, localizacao: str) -> None:
        self.localizacao = localizacao

    def andar(self) -> None:
        print(f'O Animal esta andando pelo {self.localizacao}')

class Cachorro(Mamifero):
    # Metodo especial "super"
    def __init__(self, localizacao: str) -> None:
        super().__init__(localizacao) # Se refere ao construtor da classe superior "Mamifero"

    def latir(self) -> None:
        print(f'O Cachorro está latindo; Local: {self.localizacao}')
        # self.andar()

class Gato(Mamifero):
    def __init__(self, localizacao: str) -> None:
        super().__init__(localizacao)

    def miar(self):
        print(f'O Gato está miando; Local: {self.localizacao}')

dog = Cachorro('Espanha')
dog.latir()
dog.andar()
print()

cat = Gato('Brasil')
cat.miar()
cat.andar()