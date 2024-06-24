import os
os.system('cls')

# url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
# print(f'URL: {url}')
url = ' '

#Sanitização da URL
url = url.replace(' ', '')
# url = url.strip() -> Remove os espaços em brancos de toda a string
# url = url.lstrip() -> Tira os espaços em brancos a esquerda da string
# url = url.rstrip() -> Tira os espaços em brancos a direita da string

#Validação da URL
if url == '':
    '''Retornando um erro ao usuario através do raise'''
    raise ValueError('A URL está vazia')


'''Separando a base e os parametros da url
O metodo find caso tenho dois parametros: find(1º:2º), em caso de não localizar o segundo parametro tem como retorno: '-1'
'''
indice_separador = url.find('?') # Retorna a primeira posição do ponto de interrogação não importando a sua posição, ou seja, se houvesse dois pontos de interrogação ou mais, retornaria até o primeiro que aparecer

url_base = url[0:indice_separador] # Armazenando a base da URL que é o conteúdo antes do '?', quando não é passado nenhum argumento de abertura o programa já entende que quero ir da posição inicial até o segundo parametro 
# print(f'Base da URL: {url_base}')

url_parametro = url[indice_separador + 1:] # Armazenando o parametro da URL que é o conteúdo depois do '?', quando não é passado nenhum argumento de fechamento o programa já entende que quero ir de x posição até o final dela
print(f'Parametro da URL: {url_parametro}')


'''Busca o valor de um parametro'''
parametro_busca = 'quantidade'
indice_parametro = url_parametro.find(parametro_busca)

indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametro.find('&', indice_valor) #O '&' é responsavel por separar os parametros da URL

if indice_e_comercial == -1: 
    valor = url_parametro[indice_valor]
else:
    valor = url_parametro[indice_valor:indice_e_comercial]
    
print(f'\nValor do parametro da URL, que é o conteúdo depois do "=": {valor}')