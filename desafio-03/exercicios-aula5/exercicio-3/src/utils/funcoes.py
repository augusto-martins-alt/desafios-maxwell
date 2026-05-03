import numpy as np


# Funcao que cria uma matriz de notas de alunos usando NumPy
def criar_matriz_notas():
    print("\nCadastro de notas dos alunos (3 alunos, 4 disciplinas cada)")
    notas = []

    try:
        for aluno in range(1, 4):
            print("\nAluno " + str(aluno) + ":")
            linha_notas = []
            for disciplina in range(1, 5):
                nota = float(input("  Nota da disciplina " + str(disciplina) + ": "))
                if nota < 0 or nota > 10:
                    print("Erro: a nota deve estar entre 0 e 10.")
                    return None
                linha_notas.append(nota)
            notas.append(linha_notas)

        # Converte a lista para array NumPy
        return np.array(notas)

    except ValueError:
        print("Erro: entrada invalida. Digite apenas numeros.")
        return None


# Funcao que calcula a media de cada aluno (media por linha)
def calcular_medias_alunos(matriz_notas):
    # axis=1 significa calcular a media ao longo das colunas (media de cada linha)
    medias = np.mean(matriz_notas, axis=1)
    return medias


# Funcao que calcula a media geral de cada disciplina (media por coluna)
def calcular_medias_disciplinas(matriz_notas):
    # axis=0 significa calcular a media ao longo das linhas (media de cada coluna)
    medias = np.mean(matriz_notas, axis=0)
    return medias


# Funcao que exibe a matriz de notas e as medias calculadas
def exibir_relatorio(matriz_notas, medias_alunos, medias_disciplinas):
    print("\n=== Relatorio de Notas ===\n")

    print("Matriz de Notas:")
    print(matriz_notas)
    print()

    print("Medias por Aluno:")
    for i, media in enumerate(medias_alunos):
        print("Aluno " + str(i + 1) + ": " + str(round(media, 2)))

    print("\nMedias por Disciplina:")
    for i, media in enumerate(medias_disciplinas):
        print("Disciplina " + str(i + 1) + ": " + str(round(media, 2)))
