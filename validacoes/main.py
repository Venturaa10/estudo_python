from cpf_cnpj import Documento
from acesso_cep import BuscaEndereco
import os
os.system('cls')

'''
# Testando a biblioteca
# run ->  pip install validate-docbr
from validate_docbr import CPF
cpf = CPF()
print(cpf.validate('01234567890')) # Retorna True
print(cpf.validate('23345623345')) # Retorna False
'''

'''
Testando CPF
cpf1 = Documento.cria_documento('15316264754')
print(cpf1)
# cpf2 = Documento.cria_documento('11111111111')
# print(cpf2)
'''


'''
# Testando CNPJ 
cnpj1 = Documento.cria_documento('35379838000112')
print(cnpj1)
# cnpj2 = Documento.cria_documento('11111111111111')
# print(cnpj2)
'''

cep = '01001000'
objeto_cep = BuscaEndereco(cep)
print(objeto_cep.acessa_via_cep())
