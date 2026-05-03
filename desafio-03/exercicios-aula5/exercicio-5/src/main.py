from utils.funcoes import criar_matriz_estoque, criar_matriz_precos, transpor_matriz, multiplicar_matrizes, exibir_relatorio


# Funcao principal que executa o exercicio 5
def main():
    print("========== EXERCICIO 5 ==========")
    print("Transposicao e multiplicacao de matrizes de estoque\n")
    print("Este programa calcula o valor total em estoque por loja")
    print("transpondo a matriz de estoque e multiplicando pelos precos.\n")

    # Cria a matriz de estoque
    estoque = criar_matriz_estoque()
    if estoque is None:
        return

    # Cria a matriz de precos
    precos = criar_matriz_precos()
    if precos is None:
        return

    # Transpoe a matriz de estoque (de Produtos x Lojas para Lojas x Produtos)
    estoque_transposto = transpor_matriz(estoque)

    # Multiplica a matriz transposta pelos precos
    # (Lojas x Produtos) * (Produtos x 1) = (Lojas x 1)
    valor_total = multiplicar_matrizes(estoque_transposto, precos)

    if valor_total is None:
        print("Erro: dimensoes incompativeis para multiplicacao.")
        return

    # Exibe o relatorio completo
    exibir_relatorio(estoque, estoque_transposto, precos, valor_total)

    print("\nExercicio concluido com sucesso!")


if __name__ == "__main__":
    main()
