# Usar numpy é mais recomendando quando a finalidade é trabalhar com números de maneira mais eficiente, como por exemplo trabalhando com "Data Science" / Dados
# instalação, run: pip install numpy

import array as arr
import numpy as np

arr.array('d', [1, 3.5]) 
# Primeiro argumento é o tipo do array, nesse caso é o "d" que representra numeros com pontos flutuantes (float). (Verificar Documentação)
# Segundo argumento é o array com os elementos

numeros = np.array([1, 3.5])
print(numeros)