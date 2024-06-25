import re

informacao = 'Rafaela Brasil, CPF: 718.457.190-85'

padrao = re.compile('[0-9]{3}[.]{0,1}[0-9]{3}[.]{0,1}[0-9]{3}[-]{0,1}[0-9]{2}')

verifica = padrao.search(informacao)

if verifica:
    cpf = verifica.group()
    print(f'CPF localizado: {cpf}')
else: 
    print('CPF do usuario não foi localizado!')