# Quebra do principio de Liskov
# Quando tem um comportamento diferente entre a mar e a classe filha
class Animal:
    def alimentar(self):
        print('O animal esta se alimentando...')

class Cachorro(Animal):
    def latir(self):
        print('O Cachorro esta latindo...')

class Peixe(Cachorro):
    def nadar(self):
        print('O peixe esta nadando...')

    def latir(self): # Comportamento diferente
        raise Exception('Peixe não late')


def verificar_animal(animal: any):
    animal.alimentar()
    animal.latir()

objeto1 = Animal()
objeto2 = Cachorro()
objeto3 = Peixe()
verificar_animal(objeto2)
# verificar_animal(objeto3) # O animal.latir retorna o raise Exception
