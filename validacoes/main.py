from cpf_cnpj import CpfCnpj
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

cpf1 = CpfCnpj('15316264754', 'cpf')
print(cpf1)
# cpf2 = Cpf('11111111122')
# print(cpf2)

cnpj1 = CpfCnpj('35379838000112', 'cnpj')
print(cnpj1)