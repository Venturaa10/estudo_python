'''
Elemento privado (dois underlines __): Tem nome modificado para modificado para dificultar o acesso direto e indicar que é exclusivamente de uso interno na classe
Elemento protegido (um underline _): Convenção de uso interno, mas pode ser acessado internamente pelas subclasses (classes filhas)
'''

class Mamifero:
# Observação: A classe Mamifero não consegue acessar os metodos das classes filhas
    def __init__(self, localizacao: str) -> None:
        self.localizacao = localizacao
        self._tamanho = 0.70

    def andar(self) -> None:
        print(f'O Animal esta andando pelo {self.localizacao}')

    def _dormir(self) -> None: 
        # Metodo protegido utilizando somente 1 underline
        # A convenção indica que ele deve ser chamado apenas dentro da classe ou subclasses
        # Torna possivel o acesso pelas classes filhas, permitindo que herdem e reutilizem o metodo
        print('O animal está dormindo...')

class Gato(Mamifero):
    def __init__(self, localizacao: str) -> None:
        super().__init__(localizacao)

    def miar(self):
        print(f'O Gato está miando; Local: {self.localizacao}')
        self._dormir()
        print(self._tamanho)


cat = Gato('Brasil')
cat.miar()
cat._dormir() # Deveria dar erro; Não é uma boa pratica chamar esse metodo protegido fora da classe ou de suas subclasses
