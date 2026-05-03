from utils.funcoes import criar_matriz_zeros, preencher_matriz_aleatoria, exibir_matriz


# Funcao principal que executa o exercicio 1
def main():
    print("========== EXERCICIO 1 ==========")
    print("Criando matriz 3x3 e preenchendo com numeros aleatorios\n")

    # Cria matriz 3x3 de zeros
    matriz = criar_matriz_zeros()
    exibir_matriz(matriz, "Matriz inicial (zeros):")

    # Solicita ao usuario os valores minimo e maximo para os numeros aleatorios
    try:
        valor_min = int(input("Digite o valor minimo para os numeros aleatorios: "))
        valor_max = int(input("Digite o valor maximo para os numeros aleatorios: "))

        if valor_min >= valor_max:
            print("Erro: o valor minimo deve ser menor que o valor maximo.")
            return

        # Preenche a matriz com numeros aleatorios
        matriz = preencher_matriz_aleatoria(matriz, valor_min, valor_max)
        exibir_matriz(matriz, "Matriz preenchida com numeros aleatorios:")

        print("Exercicio concluido com sucesso!")

    except ValueError:
        print("Erro: entrada invalida. Digite apenas numeros inteiros.")


if __name__ == "__main__":
    main()
