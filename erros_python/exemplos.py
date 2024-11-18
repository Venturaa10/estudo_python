def dividir(dividendo, divisor):
    if not (isinstance(dividendo, int) and isinstance(divisor, int)): # Se dividendo e divisor não forem valores inteiros, retorna um raise ValueError
        raise ValueError('dividir() deve receber apenas argumentos inteiros')
    try:
        aux = dividendo / divisor
    except:
        print(f'Não foi possivel dividir {dividendo} por {divisor}')
        raise 

    return aux

def testa_divisao(divisor):
    resultado = dividir(10, divisor)
    print(f'Resultado da divisão de 10 por {divisor} é: {resultado}')



# testa_divisao(2)
try:
    testa_divisao(2.5)

except ZeroDivisionError as E:
    print('Erro de divisão por zero!')

except Exception as E:
    print('Tratamento Generico!')

print('Programa encerrado')



# os blocos except são visitados de cima para baixo e nenhum bloco except após o except (Exception) será executado, uma vez que este captura todas as exceções do Python, ou seja, as exceções do ZeroDivisionError não serão capturados.
# try:
#     Metodo()
# except(ValueError):
#     print("ValueError")
# except(Exception):
#     print("Exception")
# except(ZeroDivisionError):
#     print("ZeroDivisionError")