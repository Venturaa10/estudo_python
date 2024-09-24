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

# Exemplo de erro
for nome, _ in usuarios: # Vai dar erro, pois na tupla existem 3 valores, e não dois
    print(f'Nome: {nome}')


