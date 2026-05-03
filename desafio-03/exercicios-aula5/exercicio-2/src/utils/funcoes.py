# Funcao que cria uma matriz de vendas com valores inseridos pelo usuario
def criar_matriz_vendas(semana):
    print("\n--- Vendas da Semana " + str(semana) + " ---")
    matriz = []

    try:
        for dia in range(1, 4):
            print("Dia " + str(dia) + ":")
            linha = []
            for produto in range(1, 4):
                valor = float(input("  Vendas do produto " + str(produto) + ": R$ "))
                if valor < 0:
                    print("Erro: o valor nao pode ser negativo.")
                    return None
                linha.append(valor)
            matriz.append(linha)
        return matriz

    except ValueError:
        print("Erro: entrada invalida. Digite apenas numeros.")
        return None


# Funcao que soma duas matrizes de mesmo tamanho
def somar_matrizes(matriz_a, matriz_b):
    matriz_soma = []
    for i in range(len(matriz_a)):
        linha = []
        for j in range(len(matriz_a[i])):
            linha.append(matriz_a[i][j] + matriz_b[i][j])
        matriz_soma.append(linha)
    return matriz_soma


# Funcao que calcula o total de vendas de uma matriz
def calcular_total_vendas(matriz):
    total = 0.0
    for linha in matriz:
        for valor in linha:
            total += valor
    return total


# Funcao que exibe a matriz formatada no console
def exibir_matriz_vendas(matriz, titulo):
    print("\n" + titulo)
    for i, linha in enumerate(matriz):
        print("Dia " + str(i + 1) + ": " + str([round(v, 2) for v in linha]))
    print()
