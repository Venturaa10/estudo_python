class SistemaCadastral:

    def cadastrar(self, nome: str, idade: str) -> None:
        if self.__validate_input(nome, idade):
            self.__register_user(nome, idade)
        else:
            self.__error_handle()

    def __validate_input(self, nome: str, idade: int) -> bool:
        ''' Valida o tipo de dado fornecido pelo usuario '''
        return isinstance(nome, str) and isinstance(idade, int)
    
    def __register_user(self, nome: str, idade: int) -> None:
        ''' Acessa e Cadastra o usuario no banco de dados '''
        print('Acessando o banco de dados...')
        print(f'Cadastrar usuario: {nome} | Idade: {idade}')

    def __error_handle(self) -> None:
        raise ValueError('Dados Invalidos!')


sistema = SistemaCadastral()
# sistema.cadastrar('João Victor Ventura', 21)
sistema.cadastrar('Vinicius', '16')