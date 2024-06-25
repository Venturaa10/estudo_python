endereco = 'Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440120'

import re # Importando o modulo para trabalhar com Expressões Regulares - RegEx

'''Cada caracter é representado por um par de colchetes [possiveis_caracteres], dentro do colchetes é informado quais os caracteres validos para o respectivo padrao, nesse caso abaixo informo que a cada caracter pode aparecer um numero do 0 ao 9, isso ocorrera cinco vez, antes do hifen e depois mais 3 caracteres
O "?" apos o caracter de hifen, é para informar que esse caracter é opcional, ou seja, o hifen pode aparecer o não no CEP informado
'''
padrao = re.compile('[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]')

busca = padrao.search(endereco) # O "padrao" de CEP será buscado na variavel "endereco" e retornara esse padrão caso ele seja localizado, em caso de não encontrado retornara "None"

if busca:
    cep = busca.group() # O metodo "group" retorna a string encontrada no padrão
    print(cep)