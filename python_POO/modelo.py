# 'modelo' é o nome dado geralmente ao arquivo que irei trabalhar com classes

class Programa:
    def __init__(self, nome, ano):
        '''Metodo construtor
        Um underline é usado como convenção, apenas para dizer ao outro programador que o atributo não deve ser acessado diretamente fora da classe
        O dulplo underline é uma forma de proteger o atributo de fato, tornando mais dificil o acesso
        '''
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        '''O decorador @property transforma o método likes em uma propriedade, permitindo que ele seja acessado como se fosse um atributo, de uma forma controlada'''
        return self._likes

    def dar_like(self):
        '''Quando esse atributo é chamado, é acrescentado 1 like ao filme / serie'''
        self._likes += 1

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        '''O decorador @nome.setter define um setter para a propriedade nome, permitindo que ela seja modificada de fora da classe '''
    
        self._nome = novo_nome.title()


class Filme(Programa):
    '''Classe Filme está herdando da classe Programa'''
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self._likes = 0


class Serie(Programa):
    '''Classe Serie está herdando da classe Programa'''
    def __init__(self, nome, ano, temporadas):
        self._nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self._likes = 0


vingadores = Filme('vingadores - guerra infinita', 2020, 160)
vingadores.dar_like()
vingadores.dar_like()
print(f'Nome: {vingadores.nome}\nAno: {vingadores.ano}\nDuração: {vingadores.duracao} Minutos\nLikes: {vingadores.likes}') 

black_mirror = Serie('black mirror', 2022, 5)
black_mirror.dar_like()
black_mirror.dar_like()
black_mirror.dar_like()
black_mirror.dar_like()

print(f'Nome: {black_mirror.nome}\nAno: {black_mirror.ano}\nTemporadas: {black_mirror.temporadas}\nLikes: {black_mirror.likes}')