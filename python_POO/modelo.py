# 'modelo' é o nome dado geralmente ao arquivo que irei trabalhar com classes

class Filme:
    def __init__(self, nome, ano, duracao):
        '''Metodo construtor'''
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

class Serie:
    def __init__(self, nome, ano, temporadas):
        '''Metodo construtor'''
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas

vingadores = Filme('Vingadores', 2020, 160)
print(vingadores.nome)