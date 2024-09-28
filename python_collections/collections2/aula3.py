import os
from collections import Counter, defaultdict
os.system('cls')

texto1 = ('''
O Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos. Isso se deve, principalmente, à sua versatilidade: ele funciona para o aprendizado de máquinas, construção de sites e até para automação de tarefas e testes de softwares.                

Além disso, sua proximidade com a linguagem humana faz com que muitas pessoas o utilizem, tanto quem desenvolve quanto quem necessariamente faz parte desse mercado.
Python é uma linguagem de programação de uso geral. Isso significa que é uma linguagem que funciona para criar uma grande variedade de aplicações diferentes.

Ou seja, o Python é uma linguagem geral, que não é especializada em nenhum problema específico.

Essa versatilidade e a facilidade de uso para pessoas iniciantes, fez com que se tornasse uma das linguagens mais comuns atualmente.
                   
O fato de ser uma linguagem interpretada, o que significa que ela não precisa passar pelo processo de compilação.

O processo de interpretação é executado dentro de máquinas virtuais, nas quais o código passa por uma camada intermediária que irá traduzir os comandos de programa para código binário.

Isso acelera bastante a velocidade de desenvolvimento.

Sua sintaxe é simples, fácil de aprender e muito próxima da linguagem falada por nós.

Por isso, podemos dizer que ela se trata de uma linguagem de alto nível.''')

texto2 = ('''
No desenvolvimento de software, a virtualização é como criar "cópias" do seu computador dentro do próprio computador. Imagine que você tem uma cozinha onde prepara diferentes tipos de comida.

Para não misturar os ingredientes, você cria estações separadas para cada receita.
A virtualização faz algo similar: cria espaços separados para que diferentes projetos de software possam ser desenvolvidos e testados sem interferir entre si.

Essa técnica é importante porque, no desenvolvimento de software, cada projeto pode ter suas próprias necessidades e dependências.

Usar a mesma "cozinha" para tudo poderia causar muitos problemas. Por exemplo, um projeto pode precisar de uma versão específica de uma biblioteca que não é compatível com outra versão usada em outro projeto… e aí teremos problemas, certo?

A virtualização permite que você tenha múltiplos ambientes, cada um configurado com as versões e dependências exatas que cada projeto precisa.

Além disso, a virtualização facilita a colaboração entre desenvolvedores. Se todos os membros da equipe usarem ambientes virtuais idênticos, será mais fácil compartilhar e testar o código sem se preocupar com diferenças na configuração dos computadores individuais.

Isso é como se todos na sua cozinha tivessem as mesmas ferramentas e ingredientes à disposição, garantindo que qualquer pessoa possa continuar a receita exatamente de onde outro parou, sem surpresas desagradáveis.

Mas como isso funciona em Python? O objetivo desse artigo é justamente explicar como usar Venv e Poetry no Python para criar e gerenciar ambientes virtuais de desenvolvimento

O Venv é uma ferramenta integrada ao Python que permite criar ambientes virtuais isolados.

Esses ambientes são importantes porque permitem que cada projeto tenha suas próprias dependências, sem interferir em outros projetos.

Isso é crucial para evitar conflitos de versão e garantir que o software funcione de maneira consistente em diferentes máquinas e configurações.

Em um mundo onde os projetos podem exigir diferentes versões de bibliotecas, o Venv torna-se uma solução simples e eficaz para gerenciar essas dependências.

O uso de Venv é recomendado pelo PEP 405 (Python Enhancement Proposal), que descreve a padronização para a criação de ambientes virtuais no Python.

O PEP 405 destaca a necessidade de isolar o ambiente de desenvolvimento para evitar que as dependências de um projeto afetem outros projetos ou o sistema global.

Seguir essas diretrizes ajuda a manter um ambiente de desenvolvimento limpo e organizado, reduzindo o risco de erros e incompatibilidades que podem surgir ao usar diferentes versões de pacotes.

Este PEP propõe adicionar ao Python um mecanismo para “ambientes virtuais” leves com seus próprios diretórios de sites, opcionalmente isolados dos diretórios de sites do sistema.

Cada ambiente virtual tem seu próprio binário Python (permitindo a criação de ambientes com várias versões Python) e pode ter seu próprio conjunto independente de pacotes Python instalados em seus diretórios de sites, mas compartilha a biblioteca padrão com o Python básico instalado.

Para utilizar o Venv, você deve primeiro criar um novo ambiente virtual. Isso pode ser feito com o comando:
''')

'''
print(Counter(texto1)) # Conta quantas vezes cada letra apareceu
print(Counter(texto1.split())) # Conta quantas vezes cada palavra apareceu
print(Counter(texto1.lower())) # Conta quantas vezes cada letra minuscula apareceu
'''
def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower()) # Armazena a contagem de quantidade de aparições de letras minusculas do texto
    total_aparicoes = sum(aparicoes.values()) # Armazena o total de letras do texto, somando todas as aparicoes

    proporcoes = [(letra, frequencia / total_aparicoes) for letra, frequencia in aparicoes.items()] # Uma lista de tuplas contendo cada letra e a proproção da sua frequencia em relação ao total de letras

    proporcoes2 = Counter(dict(proporcoes)) # Converte a lista de proporções em um Counter
    mais_comuns = proporcoes2.most_common(10) # Retorna as 10 letras mais frequentes (ou com maior proporção) no texto

    for caractere, proporcao in mais_comuns:
        print(f'{caractere} => {proporcao * 100:.2f} %')

analisa_frequencia_de_letras(texto1)
analisa_frequencia_de_letras(texto2)



