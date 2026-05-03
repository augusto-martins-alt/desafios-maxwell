# Funcao que calcula o salario de um estagiario sem aplicar descontos
def calcular_salario_estagiario(salario_fixo):
    return salario_fixo, 0.0, 0.0, salario_fixo


# Funcao que calcula o salario de um funcionario CLT aplicando INSS e IRRF
def calcular_salario_clt(salario_bruto):
    inss = salario_bruto * 0.08
    irrf = salario_bruto * 0.10 if salario_bruto > 2000 else 0.0
    salario_liquido = salario_bruto - inss - irrf
    return salario_bruto, inss, irrf, salario_liquido


# Funcao que calcula o salario de um freelancer com desconto fixo de 5%
def calcular_salario_freelancer(horas, valor_hora):
    salario_bruto = horas * valor_hora
    desconto = salario_bruto * 0.05
    salario_liquido = salario_bruto - desconto
    return salario_bruto, desconto, 0.0, salario_liquido


# Funcao que solicita os dados do funcionario, valida as entradas e retorna um dicionario
def cadastrar_funcionario():
    nome = input("Nome do funcionario: ").strip()
    if not nome:
        print("Erro: o nome nao pode ser vazio.")
        return None

    for caractere in nome:
        if not (caractere.isalpha() or caractere == " "):
            print("Erro: o nome deve conter apenas letras e espacos.")
            return None

    tipo = input("Tipo (estagiario, clt, freelancer): ").strip().lower()
    if tipo not in ("estagiario", "clt", "freelancer"):
        print("Erro: tipo invalido. Use estagiario, clt ou freelancer.")
        return None

    try:
        if tipo == "estagiario":
            salario = float(input("Salario fixo mensal (R$): "))
            if salario <= 0:
                print("Erro: salario deve ser maior que zero.")
                return None
            return {"nome": nome, "tipo": tipo, "salario": salario}

        elif tipo == "clt":
            salario = float(input("Salario bruto mensal (R$): "))
            if salario <= 0:
                print("Erro: salario deve ser maior que zero.")
                return None
            return {"nome": nome, "tipo": tipo, "salario": salario}

        elif tipo == "freelancer":
            horas = float(input("Horas trabalhadas: "))
            valor_hora = float(input("Valor por hora (R$): "))
            if horas <= 0 or valor_hora <= 0:
                print("Erro: horas e valor/hora devem ser maiores que zero.")
                return None
            return {"nome": nome, "tipo": tipo, "horas": horas, "valor_hora": valor_hora}

    except ValueError:
        print("Erro: entrada invalida. Digite apenas numeros onde solicitado.")
        return None


# Funcao que chama o calculo correto com base no tipo do funcionario e retorna um dicionario com os resultados
def processar_salario(funcionario):
    tipo = funcionario["tipo"]

    if tipo == "estagiario":
        bruto, inss, irrf, liquido = calcular_salario_estagiario(funcionario["salario"])
    elif tipo == "clt":
        bruto, inss, irrf, liquido = calcular_salario_clt(funcionario["salario"])
    elif tipo == "freelancer":
        bruto, inss, irrf, liquido = calcular_salario_freelancer(
            funcionario["horas"], funcionario["valor_hora"]
        )

    return {
        "nome": funcionario["nome"],
        "tipo": tipo.capitalize(),
        "salario_bruto": bruto,
        "inss": inss,
        "irrf": irrf,
        "salario_liquido": liquido,
    }


# Funcao que exibe o relatorio de todos os funcionarios cadastrados no console
def gerar_relatorio(funcionarios):
    if not funcionarios:
        print("Nenhum funcionario cadastrado ainda.")
        return

    print("\n=== Relatorio de Folha de Pagamento ===\n")
    total = 0.0

    for func in funcionarios:
        dados = processar_salario(func)
        total += dados["salario_liquido"]

        print("Nome: " + dados["nome"])
        print("Tipo: " + dados["tipo"])
        print("Salario Bruto:   R$ " + str(round(dados["salario_bruto"], 2)))
        print("Desconto INSS:   R$ " + str(round(dados["inss"], 2)))
        print("Desconto IRRF:   R$ " + str(round(dados["irrf"], 2)))
        print("Salario Liquido: R$ " + str(round(dados["salario_liquido"], 2)))
        print("-" * 35)

    print("\nTotal pago pela empresa: R$ " + str(round(total, 2)))


# Funcao que salva o relatorio em um arquivo de texto no diretorio informado pelo usuario
def salvar_relatorio(funcionarios):
    if not funcionarios:
        print("Nenhum funcionario cadastrado. Relatorio nao sera salvo.")
        return

    diretorio = input("Digite o diretorio onde deseja salvar o relatorio (ex: C:/Users/voce/Documents/): ").strip()
    caminho = diretorio + "relatorio_folha.txt"

    try:
        arquivo = open(caminho, "w", encoding="utf-8")
        arquivo.write("=== Relatorio de Folha de Pagamento ===\n\n")
        total = 0.0

        for func in funcionarios:
            dados = processar_salario(func)
            total += dados["salario_liquido"]

            arquivo.write("Nome: " + dados["nome"] + "\n")
            arquivo.write("Tipo: " + dados["tipo"] + "\n")
            arquivo.write("Salario Bruto:   R$ " + str(round(dados["salario_bruto"], 2)) + "\n")
            arquivo.write("Desconto INSS:   R$ " + str(round(dados["inss"], 2)) + "\n")
            arquivo.write("Desconto IRRF:   R$ " + str(round(dados["irrf"], 2)) + "\n")
            arquivo.write("Salario Liquido: R$ " + str(round(dados["salario_liquido"], 2)) + "\n")
            arquivo.write("-" * 35 + "\n")

        arquivo.write("\nTotal pago pela empresa: R$ " + str(round(total, 2)) + "\n")
        arquivo.close()

        print("Relatorio salvo com sucesso em '" + caminho + "'.")

    except OSError as erro:
        print("Erro ao salvar o arquivo: " + str(erro))