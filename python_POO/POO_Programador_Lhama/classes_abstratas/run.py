from abc import ABC, abstractmethod

class Pessoa(ABC): # Classe Abstrata não possui objetos, so pode ser mae (herança)
    def correr(self):
        print('A pessoa esta correndo de manha')

    @abstractmethod # Classe filha DEVE criar um metodo "trabalhar"
    def trabalhar(self):
        pass

# pessoa1 = Pessoa() # Vai dar error, pois uma classe abstrata só pode ser mae 
# pessoa1.correr()
# pessoa1.trabalhar()

class Professor(Pessoa):
    def trabalhar(self):
        print('O professor esta dando aula...')

class Cozinheiro(Pessoa):
    def trabalhar(self):
        print('O Cozinheiro esta cozinhando...')

pessoa2 = Professor()
pessoa2.correr()
pessoa2.trabalhar()

pessoa3 = Cozinheiro()
pessoa3.correr()
pessoa3.trabalhar()