from utils.funcoes import criar_matriz_notas, calcular_medias_alunos, calcular_medias_disciplinas, exibir_relatorio


# Funcao principal que executa o exercicio 3
def main():
    print("========== EXERCICIO 3 ==========")
    print("Matriz de notas com NumPy e calculo de medias\n")

    # Cria a matriz de notas
    matriz_notas = criar_matriz_notas()
    if matriz_notas is None:
        return

    # Calcula as medias por aluno
    medias_alunos = calcular_medias_alunos(matriz_notas)

    # Calcula as medias por disciplina
    medias_disciplinas = calcular_medias_disciplinas(matriz_notas)

    # Exibe o relatorio completo
    exibir_relatorio(matriz_notas, medias_alunos, medias_disciplinas)

    print("\nExercicio concluido com sucesso!")


if __name__ == "__main__":
    main()
