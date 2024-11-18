import re # Importando o modulo para trabalhar com Expressões Regulares - RegEx

endereco = 'Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440120'

'''Cada caracter é representado por um par de colchetes [possiveis_caracteres], dentro do colchetes é informado quais os caracteres validos para o respectivo padrao, nesse caso abaixo informo que a cada caracter pode aparecer um numero do 0 ao 9, isso ocorrera cinco vez, antes do hifen e depois mais 3 caracteres
O "-" Indica que o caracter dentro do colchetes será um número de 0 a 9
O "?" apos o caracter de hifen, é para informar que esse caracter é opcional, ou seja, o hifen pode aparecer ou não no CEP informado
As chaves "{n_vezes}" apos o caracter indica quantas vezes o parametro/caracter anterior vai ocorrer'''
padrao = re.compile(r'[0-9]{5}[-]{0,1}[0-9]{3}')

busca = padrao.search(endereco) # O "padrao" de CEP será buscado na variavel "endereco" e retornara esse padrão caso ele seja localizado, em caso de não encontrado retornara "None"

if busca:
    cep = busca.group() # O metodo "group" retorna a string encontrada no padrão
    print(cep)