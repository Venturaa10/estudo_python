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

    def __str__(self):
        '''Representação textual do objeto, esse metodo retornara uma apresentação string do objeto'''
        return f'Nome: {self.nome}\nAno: {self.ano}\nLikes: {self.likes}'


class Filme(Programa):
    '''Classe Filme está herdando da classe Programa'''
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        '''Super -> Chamando o inicializador da classe Pai (Programa), para evitar repetições do metodo construtor, tendo que acrescentar atributos que já existem na classe Programa
        O Super pode chamar qualquer metodo e atributo da classe Pai
        '''
        
        self.duracao = duracao
        
    def __str__(self):
        return f'Nome: {self.nome}\nAno: {self.ano}\nDuração: {self.duracao} Min.\nLikes: {self.likes}'

class Serie(Programa):
    '''Classe Serie está herdando da classe Programa'''
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome}\nAno: {self.ano}\nTemporadas: {self.temporadas}\nLikes: {self.likes}'

class Playlist(list):
    '''A classe vai aceitar receber uma lista como argumento, pois agora Playlist é do tipo lista'''
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)

vingadores = Filme('vingadores - guerra infinita', 2020, 160)
black_mirror = Serie('black mirror', 2022, 5)
carros = Filme('Carros', 2019, 200)
justiceiro = Serie('O Justiceiro', 2021, 8)

vingadores.dar_like()
vingadores.dar_like()
black_mirror.dar_like()
black_mirror.dar_like()
black_mirror.dar_like()
black_mirror.dar_like()
carros.dar_like()
carros.dar_like()
justiceiro.dar_like()
justiceiro.dar_like()
justiceiro.dar_like()

filmes_e_series = [vingadores, black_mirror, carros, justiceiro]
tempo_livre = Playlist('Fim de Semana', filmes_e_series)

print(f'Tamanho da Playlist: {len(tempo_livre)}\n')
for programa in tempo_livre:
    print(programa)
    print('---------------------------------------------------')

print(f'{ carros in tempo_livre}')