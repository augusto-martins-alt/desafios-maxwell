from utils.funcoes import criar_matriz_sistema, calcular_determinante, verificar_resolvibilidade, exibir_analise


# Funcao principal que executa o exercicio 4
def main():
    print("========== EXERCICIO 4 ==========")
    print("Calculando determinante e verificando resolvibilidade do sistema linear\n")
    print("Este programa analisa uma matriz 3x3 que representa um sistema linear Ax = b")
    print("e verifica se o sistema tem solucao unica atraves do determinante.\n")

    # Cria a matriz do sistema
    matriz = criar_matriz_sistema()
    if matriz is None:
        return

    # Calcula o determinante
    determinante = calcular_determinante(matriz)

    # Verifica se o sistema e resolvivel
    resolvivel, mensagem = verificar_resolvibilidade(determinante)

    # Exibe a analise completa
    exibir_analise(matriz, determinante, resolvivel, mensagem)

    print("\nExercicio concluido com sucesso!")


if __name__ == "__main__":
    main()
