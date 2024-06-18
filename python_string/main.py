import os
os.system('cls')

url = "https://bytebank.com/cambio?moedaOrigem=real"
print(f'URL: {url}')

indice_separador = url.find('?') # Retorna a posição do ponto de interrogação não importando a sua posição

url_base = url[0:indice_separador] #Armazenando a base da URL que é o conteúdo antes do '?', quando não é passado nenhum argumento de abertura o programa já entende que quero ir da posição inicial até o segundo parametro 
print(f'Base da URL: {url_base}')

url_parametro = url[indice_separador + 1:] #Armazenando o parametro da URL que é o conteúdo depois do '?', quando não é passado nenhum argumento de fechamento o programa já entende que quero ir de x posição até o final dela
print(f'Parametro da URL: {url_parametro}')