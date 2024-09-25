idades = [15, 87, 32, 65, 56, 32, 49, 37]

for i in enumerate(idades):
    print(i)

for indice, idade in enumerate(idades):
    print(indice, idade)

print(list(enumerate(idades)))


usuarios = [
    ("João Victor", 25, 1999),
    ("Vinicius", 30, 1995),
    ("Maria", 18, 2005)
]

# Desempacotando
# Esse é o recomendado, passando o nome dos elementos de forma explicita, mesmo se não for usar-las
for nome, idade, ano in usuarios:
    print(f'Nome: {nome} | Idade: {idade} | Ano: {ano}')
    print(f'Nome: {nome}')

# Desempacotando e ignorando o resto
for nome, _, _ in usuarios: # "_" O underline é uma forma de ignorar os outros valores da tupla
    print(f'Nome: {nome}')

'''
# Exemplo de erro
for nome, _ in usuarios: # Vai dar erro, pois na tupla existem 3 valores, e não dois
    print(f'Nome: {nome}')
'''

idades = [15, 87, 32, 65, 56, 32, 49, 37]
# sorted -> Ordena os valores de forma ordenada
print(sorted(idades))

# sorted(idades, reverse=True) -> Retorna os valores em ordem decrescente
print(sorted(idades, reverse=True))

# reversed -> Retorna a ordem contraria da lista
# Sem o "list" nesse caso, retornaria um objeto
print(list(reversed(idades)))

# Mesmo resultado ao se trabalhar com sorted + reverse=True
print(list(reversed(sorted(idades))))

# sort -> Modifica a lista original, ordenando os valores dela
print(idades.sort()) # Retorna None porque o metodo sort() ordena a lista in-place (modifica a lista original e não cria uma nova) e não retorna nada
print(idades) # Retorna a lista original com os valores ordenados