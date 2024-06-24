class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        '''Remove espaços em brancos e caracteres especiais da url'''
        return url.strip()

    def valida_url(self):
        if self.url == '':
            '''Retornando um erro ao usuario através do raise, se a url estiver vazia'''
            raise ValueError('A URL está vazia')
        
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


extrator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)