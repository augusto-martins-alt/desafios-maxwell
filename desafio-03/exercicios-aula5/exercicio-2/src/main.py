from utils.funcoes import criar_matriz_vendas, somar_matrizes, calcular_total_vendas, exibir_matriz_vendas


# Funcao principal que executa o exercicio 2
def main():
    print("========== EXERCICIO 2 ==========")
    print("Somando matrizes de vendas semanais\n")
    print("Cada matriz representa vendas de 3 dias com 3 produtos cada dia.\n")

    # Cria matriz de vendas da semana 1
    matriz_semana1 = criar_matriz_vendas(1)
    if matriz_semana1 is None:
        return

    # Cria matriz de vendas da semana 2
    matriz_semana2 = criar_matriz_vendas(2)
    if matriz_semana2 is None:
        return

    # Exibe as matrizes criadas
    exibir_matriz_vendas(matriz_semana1, "Vendas da Semana 1:")
    exibir_matriz_vendas(matriz_semana2, "Vendas da Semana 2:")

    # Soma as duas matrizes
    matriz_total = somar_matrizes(matriz_semana1, matriz_semana2)
    exibir_matriz_vendas(matriz_total, "Total de Vendas (Semana 1 + Semana 2):")

    # Calcula o total geral
    total_geral = calcular_total_vendas(matriz_total)
    print("Total geral de vendas: R$ " + str(round(total_geral, 2)))

    print("\nExercicio concluido com sucesso!")


if __name__ == "__main__":
    main()
