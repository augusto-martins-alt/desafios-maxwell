from utils.funcoes import cadastrar_produto, listar_produtos, realizar_venda, gerar_relatorio, salvar_relatorio


# Funcao principal que controla o menu e chama as demais funcoes
def main():
    produtos = []
    vendas = []
    opcao = 0

    while opcao != 5:
        print("\n========== MENU ==========")
        print("        LOJA SIMPLES")
        print("1 - Cadastrar produto")
        print("2 - Realizar venda")
        print("3 - Gerar relatorio")
        print("4 - Salvar relatorio em arquivo")
        print("5 - Sair")

        try:
            opcao = int(input("Digite a opcao desejada: "))
        except ValueError:
            print("Opcao invalida. Digite um numero entre 1 e 5.")
            continue

        if opcao == 1:
            cadastrar_produto(produtos)

        elif opcao == 2:
            realizar_venda(produtos, vendas)

        elif opcao == 3:
            gerar_relatorio(vendas)

        elif opcao == 4:
            salvar_relatorio(vendas)

        elif opcao == 5:
            print("Encerrando o programa. Ate logo!")

        else:
            print("Opcao invalida. Escolha entre 1 e 5.")


if __name__ == "__main__":
    main()