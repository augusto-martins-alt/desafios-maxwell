import numpy as np


# Funcao que cria uma matriz 3x3 com valores inseridos pelo usuario
def criar_matriz_sistema():
    print("\nInsira os coeficientes da matriz 3x3 do sistema linear:")
    matriz = []

    try:
        for linha in range(1, 4):
            print("\nLinha " + str(linha) + ":")
            linha_valores = []
            for coluna in range(1, 4):
                valor = float(input("  Elemento [" + str(linha) + "][" + str(coluna) + "]: "))
                linha_valores.append(valor)
            matriz.append(linha_valores)

        # Converte para array NumPy
        return np.array(matriz)

    except ValueError:
        print("Erro: entrada invalida. Digite apenas numeros.")
        return None


# Funcao que calcula o determinante de uma matriz usando NumPy
def calcular_determinante(matriz):
    determinante = np.linalg.det(matriz)
    return determinante


# Funcao que verifica se o sistema e resolvivel baseado no determinante
def verificar_resolvibilidade(determinante):
    # Um sistema linear e resolvivel se o determinante da matriz de coeficientes for diferente de zero
    # Usamos uma tolerancia pequena para evitar problemas com precisao numerica
    tolerancia = 1e-10

    if abs(determinante) < tolerancia:
        return False, "O sistema NAO tem solucao unica (determinante = 0 ou muito proximo de 0)."
    else:
        return True, "O sistema TEM solucao unica (determinante diferente de 0)."


# Funcao que exibe a matriz e os resultados da analise
def exibir_analise(matriz, determinante, resolvivel, mensagem):
    print("\n=== Analise do Sistema Linear ===\n")

    print("Matriz de Coeficientes:")
    print(matriz)
    print()

    print("Determinante: " + str(round(determinante, 6)))
    print()

    print("Status: " + mensagem)

    if resolvivel:
        print("\nComo o determinante e diferente de zero, a matriz e invertivel")
        print("e o sistema Ax = b tem solucao unica para qualquer vetor b.")
    else:
        print("\nComo o determinante e zero (ou muito proximo), a matriz e singular")
        print("e o sistema pode nao ter solucao ou ter infinitas solucoes.")
