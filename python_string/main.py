import os
os.system('cls')

url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
# print(f'URL: {url}')

indice_separador = url.find('?') # Retorna a primeira posição do ponto de interrogação não importando a sua posição, ou seja, se houvesse dois pontos de interrogação ou mais, retornaria até o primeiro que aparecer

url_base = url[0:indice_separador] # Armazenando a base da URL que é o conteúdo antes do '?', quando não é passado nenhum argumento de abertura o programa já entende que quero ir da posição inicial até o segundo parametro 
# print(f'Base da URL: {url_base}')

url_parametro = url[indice_separador + 1:] # Armazenando o parametro da URL que é o conteúdo depois do '?', quando não é passado nenhum argumento de fechamento o programa já entende que quero ir de x posição até o final dela
print(f'Parametro da URL: {url_parametro}')

parametro_busca = 'moedaOrigem'
indice_parametro = url_parametro.find(parametro_busca)

indice_valor = indice_parametro + len(parametro_busca) + 1
valor = url_parametro[indice_valor:]
print(f'Valor da URL, que é o conteúdo depois do "=": {valor}')