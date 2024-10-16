class Pessoa:
    def __init__(self, altura, idade):
        self.altura = altura
        self.idade = idade

    def correr(self):
        print(f'A primeira vez que ele correu foi com {self.idade} anos e {self.altura} de altura.')

    def comer(self):
        print(f'Comeu feijão com {self.idade} anos de idade.')


pessoa1 = Pessoa(1.73, 18)
pessoa1.correr()
pessoa1.comer()