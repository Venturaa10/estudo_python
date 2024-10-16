class MinhaClasse:
    def __init__(self, info):
        # O init é o primeiro metodo a ser chamado quando um objeto é criado
        self.atributo_1 = ['meu atributo', 20, 40, 650]
        self.atributo_2 = 'João Victor'
        self.atributo_3 = 10
        self.new_atribute = info
        print(self.new_atribute)
        
    # self -> Para se referir a classe.
    def metodo_1(self):
        print('Minha ação')

    def metodo_2(self, numero):
        print(self.atributo_3 + numero)
        print(self.atributo_1[2] + numero)
        # chamando um metodo dentro de outro metodo
        self.metodo_1()

# Objeto        # classe -> Instaciamos um objeto
minha_classe = MinhaClasse('Minha info aqui do init')

# minha_classe.metodo_1()
minha_classe.metodo_2(20)

