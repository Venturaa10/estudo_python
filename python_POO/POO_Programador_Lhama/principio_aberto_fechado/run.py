''' Principio do aberto fechado
Estabelece que "entidades de software" (classes, módulos, funções, etc.) devem ser abertaas para extensão, mas fechadas para modificação.
Isto é, a entidade pode permitir que o seu comportamento seja estendido sem modificar seu código-fonte.
'''

class Artista:
    def __init__(self, tipo: str) -> None:
        self.tipo = tipo

    def apresentar_show(self) -> None:
        print(f'O {self.tipo} esta apresentando seu show')

class Circo:
    def apresentar(self, artista: Artista) -> None:
        print('O circo esta abrindo!')
        artista.apresentar_show()
        print('O publico aplaude!')


circo = Circo()
palhaco = Artista('Palhaco')
magico = Artista('Palhaco')

circo.apresentar(magico)
circo.apresentar(palhaco)