from collections import defaultdict, Counter
'''
usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
print(assistiram)
print(len(assistiram))
assistiram.extend(usuarios_machine_learning)
print(assistiram)
print(len(assistiram))

print(set(assistiram))
'''
# Set -> Coleção não ordenada e sem duplicatas
usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

# Exibe os elementos sem duplicatas
print(usuarios_data_science | usuarios_machine_learning)

print(set([1,2,3,1,2,3,1,2,3]))
print({1,2,3,1,2,3,1,2,3})

var_set = {1,2,3,1,2,3,1,2,3,1,2,3}
print(var_set)

# Não é possivel acessar um valor pelo index, utilizando "set"
# print(var_set[2]) 

# Retorna os elementos que aparecem em ambos os conjuntos
print(usuarios_data_science & usuarios_machine_learning)

# Exibe os elementos que estão em "usuarios_data_science", mas não estão em "usuarios_machine_learning"
print(usuarios_data_science - usuarios_machine_learning)

# operador ^ em set -> Retorna os elementos que estão presentes em um conjunto ou no outro, mas não em ambos
print(usuarios_data_science ^ usuarios_machine_learning)

usuarios = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
print(len(usuarios))

# add -> Adiciona um valor ao conjunto
usuarios.add(25)
usuarios.add(5) # Esse elemento já está dentro do conjunto, então não vai adicionar
print(usuarios)
print(len(usuarios))

# Conjunto congelado
# frozenset -> Conjunto imutavel e de elementos unicos
usuarios2 = frozenset({1,2,3,4,5,6,7,8,9,10,11,12,13,14,15})
print(usuarios2)

'''
# Retorna erro, pois não aceita "add" em um conjunto congelado
usuarios2.add(25) 
'''

meu_texto = "Bem vindo meu nome é João Victor eu gosto muito de futebol e tenho o meu gatos e gosto muito de gatos"
print(meu_texto.split()) # Repete palavras
print(set(meu_texto.split())) # Não repete palavras
meu_texto = meu_texto.lower()

# defaultdict -> Utilizado para trabalhar com um dicionario com valor padrão
aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    # Contando o número de vezes que uma palavra aparece
    aparicoes[palavra] += 1


print(aparicoes['vinicius']) # Retorna 0, por causa do "int", pois a cahve não existe no dicionario
print(aparicoes)

class Conta:
    def __init__(self):
        print('Criando uma conta')

contas = defaultdict(Conta)
print(contas[15])

# Utilizando "Counter" para contar as aparições de palavras, em um codigo bem menor, comparado ao uso do for para a mesma finalidade
aparicoes2 = Counter(meu_texto.split())
print(aparicoes2)