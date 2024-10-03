from telefone_br import TelefonesBr
import re

telefone = "552126481234"

telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)
'''
# A variável 'padrao' define o formato esperado de um número de telefone
padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
resposta = re.search(padrao,telefone)
print(resposta.group())

# 'resposta.group(n)' retorna o conteúdo de um grupo especifico:
print(resposta.group(1)) 
print(resposta.group(2))
print(resposta.group(3))
'''
