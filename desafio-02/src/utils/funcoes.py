# Funcao que cadastra um produto e retorna um dicionario com seus dados
def cadastrar_produto(produtos):
    """
    Solicita dados do produto e adiciona na lista de produtos.
    Retorna True se cadastrado com sucesso, False caso contrario.
    """
    print("\n--- Cadastrar Produto ---")
    
    # Solicita e valida o nome do produto
    nome = input("Nome do produto: ").strip()
    if not nome:
        print("Erro: o nome nao pode ser vazio.")
        return
    
    # Solicita e valida o preco
    try:
        preco = float(input("Preco unitario (R$): "))
        if preco <= 0:
            print("Erro: o preco deve ser maior que zero.")
            return
    except ValueError:
        print("Erro: digite um valor numerico valido para o preco.")
        return
    
    # Solicita e valida o estoque inicial
    try:
        estoque = int(input("Quantidade em estoque: "))
        if estoque < 0:
            print("Erro: o estoque nao pode ser negativo.")
            return
    except ValueError:
        print("Erro: digite um numero inteiro valido para o estoque.")
        return
    
    # Cria o dicionario do produto
    produto = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }
    
    # Adiciona o produto na lista
    produtos.append(produto)
    print(f"Produto '{nome}' cadastrado com sucesso!")


# Funcao que lista todos os produtos cadastrados
def listar_produtos(produtos):
    """
    Exibe a lista de produtos com seus indices, nomes, precos e estoque.
    Retorna True se ha produtos, False se nao ha.
    """
    if not produtos:
        print("\nNenhum produto cadastrado ainda.")
        return False
    
    print("\n--- Produtos Disponiveis ---")
    for i, produto in enumerate(produtos):
        print(f"{i + 1} - {produto['nome']} | R$ {produto['preco']:.2f} | Estoque: {produto['estoque']}")
    
    return True


# Funcao que calcula o valor da venda com desconto se aplicavel
def calcular_valor_venda(preco, quantidade):
    """
    Calcula o valor total da venda.
    Aplica desconto de 5% se quantidade > 10.
    Retorna tupla (valor_total, desconto_aplicado, percentual_desconto)
    """
    valor_bruto = preco * quantidade
    
    # Aplica desconto de 5% se quantidade maior que 10
    if quantidade > 10:
        percentual = 5
        desconto = valor_bruto * 0.05
        valor_total = valor_bruto - desconto
    else:
        percentual = 0
        desconto = 0.0
        valor_total = valor_bruto
    
    return valor_total, desconto, percentual


# Funcao que realiza uma venda
def realizar_venda(produtos, vendas):
    """
    Realiza uma venda: solicita cliente, produto, quantidade,
    valida estoque, calcula valor e registra a venda.
    """
    print("\n--- Realizar Venda ---")
    
    # Verifica se ha produtos cadastrados
    if not produtos:
        print("Erro: nenhum produto cadastrado ainda. Cadastre produtos primeiro.")
        return
    
    # Solicita nome do cliente
    cliente = input("Nome do cliente: ").strip()
    if not cliente:
        print("Erro: o nome do cliente nao pode ser vazio.")
        return
    
    # Lista os produtos disponiveis
    listar_produtos(produtos)
    
    # Solicita a selecao do produto
    try:
        escolha = int(input("\nEscolha o numero do produto: "))
        
        # Valida o indice
        if escolha < 1 or escolha > len(produtos):
            print("Erro: produto inexistente. Escolha um numero valido da lista.")
            return
        
        # Pega o produto selecionado (ajusta indice)
        produto_selecionado = produtos[escolha - 1]
        
    except ValueError:
        print("Erro: digite um numero inteiro valido.")
        return
    
    # Solicita a quantidade
    try:
        quantidade = int(input("Quantidade desejada: "))
        if quantidade <= 0:
            print("Erro: a quantidade deve ser maior que zero.")
            return
    except ValueError:
        print("Erro: digite um numero inteiro valido para a quantidade.")
        return
    
    # Verifica se ha estoque suficiente
    if quantidade > produto_selecionado["estoque"]:
        print(f"Erro: estoque insuficiente. Disponivel: {produto_selecionado['estoque']} unidades.")
        return
    
    # Calcula o valor da venda
    valor_total, desconto, percentual = calcular_valor_venda(
        produto_selecionado["preco"], 
        quantidade
    )
    
    # Atualiza o estoque
    produto_selecionado["estoque"] -= quantidade
    
    # Registra a venda
    venda = {
        "cliente": cliente,
        "produto": produto_selecionado["nome"],
        "quantidade": quantidade,
        "preco_unitario": produto_selecionado["preco"],
        "desconto": desconto,
        "percentual_desconto": percentual,
        "valor_total": valor_total
    }
    
    vendas.append(venda)
    
    # Exibe confirmacao da venda
    print("\n=== Venda Realizada com Sucesso ===")
    print(f"Cliente: {cliente}")
    print(f"Produto: {produto_selecionado['nome']}")
    print(f"Quantidade: {quantidade}")
    print(f"Preco unitario: R$ {produto_selecionado['preco']:.2f}")
    
    if percentual > 0:
        print(f"Desconto aplicado: {percentual}% (R$ {desconto:.2f})")
    
    print(f"Valor total: R$ {valor_total:.2f}")
    print("=" * 35)


# Funcao que gera o relatorio de vendas
def gerar_relatorio(vendas):
    """
    Exibe o relatorio completo de todas as vendas realizadas
    e o total arrecadado pela loja.
    """
    if not vendas:
        print("\nNenhuma venda realizada ainda.")
        return
    
    print("\n" + "=" * 50)
    print("         RELATORIO DE VENDAS")
    print("=" * 50)
    
    total_arrecadado = 0.0
    
    for i, venda in enumerate(vendas, 1):
        print(f"\nVenda #{i}")
        print(f"Cliente: {venda['cliente']}")
        print(f"Produto: {venda['produto']}")
        print(f"Quantidade: {venda['quantidade']}")
        print(f"Preco unitario: R$ {venda['preco_unitario']:.2f}")
        
        if venda['percentual_desconto'] > 0:
            print(f"Desconto: {venda['percentual_desconto']}% (R$ {venda['desconto']:.2f})")
        
        print(f"Valor total: R$ {venda['valor_total']:.2f}")
        print("-" * 50)
        
        total_arrecadado += venda['valor_total']
    
    print(f"\nTotal arrecadado pela loja: R$ {total_arrecadado:.2f}")
    print("=" * 50)


# Funcao que salva o relatorio em arquivo de texto
def salvar_relatorio(vendas):
    """
    Salva o relatorio de vendas em um arquivo de texto
    no diretorio especificado pelo usuario.
    """
    if not vendas:
        print("\nNenhuma venda realizada. Relatorio nao sera salvo.")
        return
    
    diretorio = input("Digite o diretorio onde deseja salvar o relatorio (ex: /home/usuario/): ").strip()
    
    # Se o diretorio nao terminar com /, adiciona
    if diretorio and not diretorio.endswith("/"):
        diretorio += "/"
    
    caminho = diretorio + "relatorio_vendas.txt"
    
    try:
        arquivo = open(caminho, "w", encoding="utf-8")
        
        arquivo.write("=" * 50 + "\n")
        arquivo.write("         RELATORIO DE VENDAS\n")
        arquivo.write("=" * 50 + "\n")
        
        total_arrecadado = 0.0
        
        for i, venda in enumerate(vendas, 1):
            arquivo.write(f"\nVenda #{i}\n")
            arquivo.write(f"Cliente: {venda['cliente']}\n")
            arquivo.write(f"Produto: {venda['produto']}\n")
            arquivo.write(f"Quantidade: {venda['quantidade']}\n")
            arquivo.write(f"Preco unitario: R$ {venda['preco_unitario']:.2f}\n")
            
            if venda['percentual_desconto'] > 0:
                arquivo.write(f"Desconto: {venda['percentual_desconto']}% (R$ {venda['desconto']:.2f})\n")
            
            arquivo.write(f"Valor total: R$ {venda['valor_total']:.2f}\n")
            arquivo.write("-" * 50 + "\n")
            
            total_arrecadado += venda['valor_total']
        
        arquivo.write(f"\nTotal arrecadado pela loja: R$ {total_arrecadado:.2f}\n")
        arquivo.write("=" * 50 + "\n")
        
        arquivo.close()
        
        print(f"\nRelatorio salvo com sucesso em '{caminho}'.")
        
    except OSError as erro:
        print(f"Erro ao salvar o arquivo: {erro}")