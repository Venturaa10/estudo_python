import re

class ExtratorURL:
    ''' Classe responsavel por indentificar e extrair as informações da URL'''
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        '''
        Remove espaços em brancos e caracteres especiais da url
        Caso o tipo da url seja diferente do tipo string, significa que a url está vazia, logo retornara como vazio para o metodo valida_url
        '''
        if type(url) == str:
            return url.strip()
        else:
            return ''
        

    def valida_url(self):
        '''Quando não existir uma URL, vai retornar um ValueError
        É recomendado verificar se uma string é vazia utilizando o "not" com a primeira validação
        '''
        if not self.url:
            '''Retornando um erro ao usuario através do raise, se a url estiver vazia'''
            raise ValueError('A URL está vazia')
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        verifica = padrao_url.match(self.url)

        if not verifica:
            raise ValueError('A URL não é valida')

    def get_url_base(self):
        '''Separando a base e os parametros da url
        O metodo find caso tenho dois parametros: find(1º:2º), em caso de não localizar o segundo parametro tem como retorno: '-1'
        '''
        indice_separador = self.url.find('?')
        url_base = self.url[0:indice_separador]
        return url_base 

    def get_url_parametro(self):
        indice_separador = self.url.find('?')
        url_parametro = self.url[indice_separador + 1:]
        return url_parametro

    def get_valor_parametro(self, parametro_busca):
        '''Busca o valor de um parametro'''
        indice_parametro = self.get_url_parametro().find(parametro_busca)

        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametro().find('&', indice_valor) #O '&' é responsavel por separar os parametros da URL

        if indice_e_comercial == -1: 
            valor = self.get_url_parametro()[indice_valor]
            return valor
        else:
            valor = self.get_url_parametro()[indice_valor:indice_e_comercial]
            return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f'URL: {self.url}\nURL Base: {self.get_url_base()}\nParametros: {self.get_url_parametro()}'

    def __eq__(self, orther):
        '''
        Metodo especial para verificar se existe igualdade entre os objetos fornecidos
        O primeiro parametro é o objeto atual, o segundo é outro objeto que será comparado
           '''
        return self.url == orther.url
    

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
extrator_url2 = ExtratorURL(url)

print(extrator_url == extrator_url2)
print(f'O tamanho da URL: {len(extrator_url)}')
print(extrator_url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)

''' Dois objetos podem ser iguais (O valor), mas não identicos (End. de Memoria diferentes )'''
print(id(extrator_url)) # Imprimindo o endereço de memoria do objeto com o metodo "id"
print(id(extrator_url2))

'''Verificar se dois objetos são realmente identicos utilizando o metodo "is", ou seja, a comparação é feita entre o endereço de memoria dos objetos 
"==" -> Verifica se os valores são equivalentes
"is" -> Verifica se os dois objetos são o mesmo na memória
'''
1 is True