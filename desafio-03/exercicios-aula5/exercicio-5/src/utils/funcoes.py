import numpy as np


# Funcao que cria uma matriz de estoque (produtos x lojas)
def criar_matriz_estoque():
    print("\nCadastro de estoque (3 produtos, 2 lojas)")
    print("Cada linha representa um produto, cada coluna uma loja\n")
    estoque = []

    try:
        for produto in range(1, 4):
            print("Produto " + str(produto) + ":")
            linha = []
            for loja in range(1, 3):
                quantidade = int(input("  Quantidade na loja " + str(loja) + ": "))
                if quantidade < 0:
                    print("Erro: a quantidade nao pode ser negativa.")
                    return None
                linha.append(quantidade)
            estoque.append(linha)

        # Converte para array NumPy
        return np.array(estoque)

    except ValueError:
        print("Erro: entrada invalida. Digite apenas numeros inteiros.")
        return None


# Funcao que cria uma matriz de precos (produtos)
def criar_matriz_precos():
    print("\nCadastro de precos dos produtos")
    precos = []

    try:
        for produto in range(1, 4):
            preco = float(input("Preco do produto " + str(produto) + ": R$ "))
            if preco <= 0:
                print("Erro: o preco deve ser maior que zero.")
                return None
            precos.append([preco])

        # Converte para array NumPy (matriz coluna 3x1)
        return np.array(precos)

    except ValueError:
        print("Erro: entrada invalida. Digite apenas numeros.")
        return None


# Funcao que transpoe uma matriz usando NumPy
def transpor_matriz(matriz):
    return matriz.T


# Funcao que multiplica duas matrizes usando NumPy
def multiplicar_matrizes(matriz_a, matriz_b):
    # Verifica se as dimensoes sao compativeis para multiplicacao
    if matriz_a.shape[1] != matriz_b.shape[0]:
        return None
    return np.dot(matriz_a, matriz_b)


# Funcao que exibe o relatorio completo da analise
def exibir_relatorio(estoque, estoque_transposto, precos, valor_total):
    print("\n=== Relatorio de Estoque e Valores ===\n")

    print("Matriz de Estoque Original (Produtos x Lojas):")
    print("Linhas = Produtos, Colunas = Lojas")
    print(estoque)
    print()

    print("Matriz de Estoque Transposta (Lojas x Produtos):")
    print("Linhas = Lojas, Colunas = Produtos")
    print(estoque_transposto)
    print()

    print("Matriz de Precos (Produtos):")
    print(precos)
    print()

    print("Valor Total em Estoque por Loja:")
    print("(Estoque Transposto x Precos)")
    for i, valor in enumerate(valor_total):
        print("Loja " + str(i + 1) + ": R$ " + str(round(valor[0], 2)))

    total_geral = np.sum(valor_total)
    print("\nValor Total Geral em Estoque: R$ " + str(round(total_geral, 2)))
