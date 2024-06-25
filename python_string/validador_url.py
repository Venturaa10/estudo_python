import re
'''
Exemplos de URLs válidas:

bytebank.com/cambio
bytebank.com.br/cambio
www.bytebank.com/cambio
www.bytebank.com.br/cambio
http://www.bytebank.com/cambio
http://www.bytebank.com.br/cambio
https://www.bytebank.com/cambio
https://www.bytebank.com.br/cambio

Exemplos de URLs inválidas:

https://bytebank/cambio
https://bytebank.naoexiste/cambio
ht://bytebank.naoexiste/cambio
'''

url = 'www.bytebank.com.br/cambio'

''' Os parenteses é para indicar que o valor deve ser exatamente igual ao que está dentro dos pareteses (valor_igual_obrigatorio) '''

padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')

verifica = padrao_url.match(url)

if not verifica:
    raise ValueError('A URL não é valida')

# print(f'A URL "{verifica}" é válida')
print('A URL é válida')