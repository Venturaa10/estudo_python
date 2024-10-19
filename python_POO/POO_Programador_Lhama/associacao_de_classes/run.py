class Interruptor:
    def __init__(self, comodo:str):
        self.comodo = comodo

    def acender(self) -> None:
        print(f'Estou acendendo a luz do comodo: {self.comodo}')

    def apagar(self) -> None:
        print(f'Estou apagando a luz do comodo: {self.comodo}')


casa = Interruptor('Sala')
casa.acender()
casa.apagar()

class Pessoa():
    ''' A classe Pessoa esta utilizando metodos de outra classe (Interruptor)'''
    def acender_luzes(self, interruptor:Interruptor) -> None: 
        interruptor.acender() # Metodo da classe Interruptor

    def apagar_luzes(self, interruptor:Interruptor) -> None:
        interruptor.apagar()

    def dormir(self) -> None:
        print('A pessoa foi dormir')

joao = Pessoa()
interruptor_sala = Interruptor('Quarto')

joao.acender_luzes(interruptor_sala)
