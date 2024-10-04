from datetime import datetime, timedelta
import os
from datas_br import DatasBr
os.system('cls')

print(datetime.today()) # Retorna a hora exata que o codigo é executado

cadastro = DatasBr()
print(cadastro.momento_cadastro)
print(cadastro.mes_cadastro())
print(cadastro.dia_semana())
print(cadastro)


'''
hoje = datetime.today()
# Formatando para o formato BR
hoje_formatado = hoje.strftime('%d/%m/%Y %H:%M') 
print(hoje)
print(hoje_formatado)
'''