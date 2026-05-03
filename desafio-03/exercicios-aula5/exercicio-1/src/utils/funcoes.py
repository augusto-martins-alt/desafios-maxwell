import random


# Funcao que cria uma matriz 3x3 preenchida com zeros
def criar_matriz_zeros():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(0)
        matriz.append(linha)
    return matriz


# Funcao que preenche a matriz com numeros aleatorios entre um valor minimo e maximo
def preencher_matriz_aleatoria(matriz, valor_min, valor_max):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = random.randint(valor_min, valor_max)
    return matriz


# Funcao que exibe a matriz formatada no console
def exibir_matriz(matriz, titulo):
    print("\n" + titulo)
    for linha in matriz:
        print(linha)
    print()
