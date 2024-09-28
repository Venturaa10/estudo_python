from cpf import Cpf
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

cpf1 = Cpf('15316264754')
print(cpf1)
# cpf2 = Cpf('11111111122')
# print(cpf2)
