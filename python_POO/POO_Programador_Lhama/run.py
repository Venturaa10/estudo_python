# Trabalhando com Metodos Privados

# Metodos com dois underlines, possuem a propriedade de tornar o metodo privado, são acessados apenas dentro da propria classe
# exemplo: __nome_metodo
class Pessoa:
    def __init__(self, altura, cpf):
        self.altura = altura
        self.cpf = cpf

    def apresentar(self):
        print(f'Olá! Minha altura - {self.altura}')
        self.__coletar_documento() # Acessando o metodo privado dentro de outro metodo da classe

    def __coletar_documento(self):
        # Metodo privado, para exibir o cpf do usuario
        print(f'Meu documento - {self.cpf}')    

joao = Pessoa('1.75', 'fadfdasvsda')
# joao.__coletar_documento() # Saída: erro
joao.apresentar() # Saída: Sucesso