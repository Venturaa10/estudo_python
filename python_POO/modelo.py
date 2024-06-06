# 'modelo' é o nome dado geralmente ao arquivo que irei trabalhar com classes

class Filme:
    def __init__(self, nome, ano, duracao):
        '''Metodo construtor'''
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    def dar_like(self):
        self.likes += 1


class Serie:
    def __init__(self, nome, ano, temporadas):
        '''Metodo construtor'''
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_like(self):
        self.likes += 1


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