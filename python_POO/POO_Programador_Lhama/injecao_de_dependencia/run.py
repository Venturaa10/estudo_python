'''Injeção de Dependência
Relacionamento de classes através do metodo construtor


 '''

class Celular:
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo

    def enviar_mensagem(self, mensagem: str) -> None:
        print(f'Enviando mensagem: {mensagem}')

    def abrir_emails(self) -> None:
        print('Abrindo os emails...')

    def abrir_youtube(self):
        print('Abrindo Youtube...')

class Pessoa:
    def __init__(self, celular: Celular) -> None:
        ''' É recomendado que dependencias sejam tratadas como elementos privados '''
        self.__celular = celular # Dependencia

    def pedir_pizza(self) -> None:
        print('Buscando o celular...')
        print('Definindo o sabor...')
        self.__celular.enviar_mensagem('Quero uma de calabreza')
        print('Pedido realizado!')

    def estudar(self) -> None:
        print('Ligando o computador...')
        self.__celular.abrir_youtube()
        print('Iniciando os estudos')

android = Celular('Motorola')
iphone = Celular('Iphone')

joao = Pessoa(android)
marlene = Pessoa(iphone)
print('\nJoão...')
joao.pedir_pizza()
print('\nMarlene...')
marlene.estudar()