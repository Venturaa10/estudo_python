from cpf_cnpj import Documento
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

cpf1 = Documento.cria_documento('15316264754')
print(cpf1)
# cpf2 = Documento.cria_documento('11111111111')
# print(cpf2)


cnpj1 = Documento.cria_documento('35379838000112')
print(cnpj1)
# cnpj2 = Documento.cria_documento('11111111111111')
# print(cnpj2)
