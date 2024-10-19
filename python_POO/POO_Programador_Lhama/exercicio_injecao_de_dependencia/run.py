class ConectorBancoDeDados:
    def __init__(self) -> None:
        self.connection = None

    def conectar_ao_banco(self) -> None:
        self.connection = True


class RepositorioDeBanco:
    def __init__(self, conexao: ConectorBancoDeDados) -> None:
        self.__conexao = conexao

    def busca_dados(self) -> list:
        if self.__conexao.connection:
            print('Conexão realizada com sucesso!')
            return [1, 2, 3, 4, 5]
        
        return None
    
class RegraDeNegocio:
    def __init__(self, repo: RepositorioDeBanco) -> None:
        self.__repo = repo

    def calcular_resultados(self) -> None:
        dados = self.__repo.busca_dados()

        if not dados:
            print('Dados não encontrados. Verifique sua conexão com o banco')

        else:
            resposta = 0
            for dado in dados:
                resposta += dado

            print(f'O resultado: {resposta}')


# Cada classe esta dependendo da outra 
conn = ConectorBancoDeDados() 
conn.conectar_ao_banco() # Conectando ao banco

repo = RepositorioDeBanco(conn) # Colocando banco no repositorio
repo.busca_dados()

regra = RegraDeNegocio(repo) # Colocando o repositorio dentro da regra
regra.calcular_resultados()