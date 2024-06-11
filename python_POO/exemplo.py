# Exemplo simples para ver como funciona herança multipla

class Funcionario:
    def __init__(self, nome):
        self.nome = nome 
        
    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


class Hipster:
    '''Mixin, fornece metodos adicionais sem influenciar diretamente a hierarquia de herança principal, sendo instaciada por si só'''
    def __str__(self):
        return f'Hipster, {self.nome}'


class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    '''Coloco entre virgulas quando tiver mais de uma classe a ser herdada'''
    pass

class Senior(Alura, Caelum, Hipster):
    pass

bruno = Senior('Bruno')
print(bruno)

vinicius = Junior() 
vinicius.busca_perguntas_sem_resposta()

joao = Pleno() # João como Pleno e herdando de Alura e Caelum, consegue acessar atributos de ambas as classes
joao.busca_perguntas_sem_resposta()
joao.busca_cursos_do_mes()
joao.mostrar_tarefas() #Exibe o atributo em Alura devido a ordem que a class Pleno está herdando, sendo chamado primeiro Alura

michelle = Senior()
michelle.mostrar_tarefas() #Exibe o atributo em Caelum devido a ordem que a class Senior está herdando, sendo chamado primeiro Caelum

# MRO - Algoritmo
# Pleno > Aura > Caelum (GoodHead)> Funcionario