
teste_dic = {'nome' : 'João Victor', 'time' : 'Flamengo', 'estado' : 'Rio de Janeiro' }
'''
print(teste_dic['nome'])
print(teste_dic['time'])
print(teste_dic.get('estado')) # Retorna o valor da chave
print(teste_dic.get('idade')) # Retorna None, pois não existe essa chave no dicionario 

for i in teste_dic.keys():
    valor = teste_dic[i]
    print(i, valor)

for i in teste_dic.values():
    print(i)
'''

for i in teste_dic.items():
    print(i)

for chave, valor in teste_dic.items():
    print(f'{chave} : {valor}')

# Criando utilizando"dict"
teste_dic2 = dict(nome = 'Vinicius', time = 'Flamengo', estado = 'RJ')
print(teste_dic2)

teste_dic2['nome'] = 'Carlos' # Atribuindo um novo elemento a chave
print(teste_dic2)

del teste_dic2['nome'] # Removendo uma chave:valor do dicionario
print(teste_dic2)

print('nome' in teste_dic2 )
print('time' in teste_dic2 )
