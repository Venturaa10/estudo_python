import os
os.system('cls')

# Coleções -> Usados para trabalhar com diversos valores

# Lista com idades
idades = [39, 30, 25, 17]
print(type(idades)) # Qual é o tipo da variavel "idades"
print(len(idades)) # Tamanho da lista
print(idades)

idades.append(15) # Adicionando um valor no fim da lista
print(f'Lista Atualizada: {idades}')

# for idade in idades: # Imprimindo cada elemento da lista separadamente
#     print(idade)

idades.remove(25) # Removendo um valor já existente \ especifico dentro da lista
print(f'Idades após remover um elemento: {idades}')

if 17 not in idades:
    print('O valor 17 não existe na lista "idades"!')
else:
    idades.remove(17)
    print(f'Lista atualizada após remover o valor 17: {idades}')

# idades.clear() # Limpando | Removendo todos os valores da lista
# print(f'Lista vazia: {idades}')

idades.insert(2, 10) # Adicionando um valor em uma determinada posição (index) na lista (index,valor)
print(idades)

idades.extend([3,6,8,9,10,37,40,25,22,31]) # Adcionando varios valores de uma só vez na lista
print(f'Lista idade após o uso do metodo "extend": {idades}')
print(f'Tamanho da lista atualizada após o "extend": {len(idades)}')

# list comprehension -> permite construir listas a partir de sequências existentes, aplicando uma expressão e\ou adicionando filtros.
print('\nCriando uma nova lista com as idades após o aniversario dos usuarios')
# 1º Maneira
forma_1 = []
for idade in idades:
    forma_1.append(idade + 1)
print(f'1º Maneira: {forma_1}')

# 2º Maneira
forma_2 = []
[forma_2.append(idade + 1) for idade in idades]
print(f'2º Maneira: {forma_2}')

# 3º Maneira
forma_3 = [idade + 1 for idade in idades]
print(f'3º Maneira: {forma_3}')

print(f'\nBuscando apenas idades maiores que 21 anos: {[(idade) for idade in forma_3 if idade > 21]}')

# Pratica recomendada -> Passar uma lista (ou qualquer objeto mutável) como None e inicializá-la dentro da função é uma boa prática, evitando problemas relacionados á mutabilidade dos objetos.
def teste_mutabilidade(lista = None): # Pratica recomendada
    if lista == None: # Verifica se a lista é None
        lista = list() # Inicializa uma nova lista vazia

    print(len(lista)) # Imprime o comprimento da lista
    lista.append(10) # Adiciona o número 10 a lista

teste_mutabilidade()
teste_mutabilidade()
teste_mutabilidade()
teste_mutabilidade()
teste_mutabilidade()
teste_mutabilidade()

'''
# Pratica NÃO recomendada
def teste_mutabilidade(lista = []):  # Lista vazia como valor padrão (NÃO RECOMENDADO)
    print(len(lista))
    lista.append(10)

teste_mutabilidade()  # Imprime 0, adiciona 10
teste_mutabilidade()  # Imprime 1, adiciona 10
teste_mutabilidade()  # Imprime 2, adiciona 10
teste_mutabilidade()  # Imprime 3, adiciona 10
teste_mutabilidade()  # Imprime 4, adiciona 10
'''
