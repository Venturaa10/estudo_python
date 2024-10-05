# Instalação, run -> pip install requests
import requests
from acesso_cep import BuscaEndereco

r = requests.get('https://viacep.com.br/ws/01001000/json/')

# Retorna: Response[200], Significa que a requisição funcionou
print(r) 
print(dir(r)) # Retorna todos os atributos / metodos do objeto, por exemplo o .text, .json
print(type(r))
print(type(r.text)) # Retorna string


print(type(r.json())) # Retorna dict
print(r.json()['cep']) # Buscando o valor de uma chave do dicionario
print((r.text))