from utils.funcoes import cadastrar_funcionario, gerar_relatorio, salvar_relatorio


# Funcao principal que controla o menu e chama as demais funcoes
def main():
    funcionarios = []
    opcao = 0

    while opcao != 4:
        print("\n========== MENU ==========")
        print("     FOLHA DE PAGAMENTO")
        print("1 - Cadastrar funcionario")
        print("2 - Gerar relatorio")
        print("3 - Salvar relatorio em arquivo")
        print("4 - Sair")

        try:
            opcao = int(input("Digite a opcao desejada: "))
        except ValueError:
            print("Opcao invalida, tente novamente!")
            continue

        if opcao == 1:
            func = cadastrar_funcionario()
            if func:
                funcionarios.append(func)
                print("Funcionario '" + func["nome"] + "' cadastrado com sucesso!")

        elif opcao == 2:
            gerar_relatorio(funcionarios)

        elif opcao == 3:
            salvar_relatorio(funcionarios)

        elif opcao == 4:
            print("Encerrando o programa. Ate logo!")

        else:
            print("Opcao invalida, tente novamente!")


if __name__ == "__main__":
    main()