import os

decisao = 0
while (decisao != 5):
    print("===== CENTRAL DE ESTOQUE =====")
    print("1 > Novo Registro")
    print("2 > Exibir Inventário")
    print("3 > Remover Item")
    print("4 > Registrar Saída/Venda")
    print("5 > Encerrar Sistema")
    print("==============================")

    decisao = int(input("Selecione uma operação: "))

    if (decisao == 1):
        print("\n--- FORMULÁRIO DE CADASTRO ---")
        ref_id = input("ID do item: ")
        descricao = input("Descrição do item: ")
        valor_unit = input("Valor unitário: ")
        volume_estoque = input("Volume inicial: ")

    
        banco_dados = open("estoque_geral.txt", "a")
        banco_dados.write(f"{ref_id}|{descricao}|{valor_unit}|{volume_estoque}\n")
        banco_dados.close()
        
        print("\n[OK] Registro salvo com sucesso!")
        input("\nPressione qualquer tecla para voltar...")
        os.system("cls")

    elif (decisao == 2):
        print("\n--- RELATÓRIO DE INVENTÁRIO ---")
        
        
        if os.path.exists("estoque_geral.txt"):
            banco_dados = open("estoque_geral.txt", "r")
            for entrada in banco_dados:
                id_prod, desc_prod, val_prod, qtd_prod = entrada.strip().split("|")
                print(f"ID: {id_prod} | Produto: {desc_prod}")
                print(f"Preço: R$ {val_prod} | Em Estoque: {qtd_prod}")
                print("-" * 30)
            banco_dados.close()
        else:
            print("Nenhum registro encontrado.")

        input("\nPressione Enter para continuar...")
        os.system("cls")

    elif (decisao == 3):
        print("\n--- EXCLUSÃO DE REGISTRO ---")
        banco_dados = open("estoque_geral.txt", "r")
        lista_itens = banco_dados.readlines()
        banco_dados.close()

        num_linha = int(input("Informe o índice da linha para deletar: "))
        posicao = num_linha - 1
        
        if 0 <= posicao < len(lista_itens):
            item_deletado = lista_itens.pop(posicao)
            
            banco_dados = open("estoque_geral.txt", "w")
            for registro in lista_itens:
                banco_dados.write(registro)
            banco_dados.close()
            print(f"\n[!] Registro removido.")
        else:
            print("\n[Erro] Linha inválida.")

        input("\nRetornar ao menu...")
        os.system("cls")

    elif decisao == 4:
        print("\n--- MOVIMENTAÇÃO DE VENDA ---")

        busca_item = input("Nome do produto vendido: ")
        demanda = int(input("Quantidade comercializada: "))

        banco_dados = open("estoque_geral.txt", "r")
        historico = banco_dados.readlines()
        banco_dados.close()

        banco_dados = open("estoque_geral.txt", "w")
        localizado = False
        
        for linha_atual in historico:
            colunas = linha_atual.strip().split("|")

            if len(colunas) == 4:
                id_f, nome_f, preco_f, estoque_f = colunas
                estoque_f = int(estoque_f)

                if nome_f == busca_item:
                    localizado = True
                    if estoque_f >= demanda:
                        estoque_f -= demanda
                        print(f"\n[Sucesso] Baixa de {demanda} unidades aplicada.")
                    else:
                        print(f"\n[Aviso] Saldo insuficiente! (Disponível: {estoque_f})")

                banco_dados.write(f"{id_f}|{nome_f}|{preco_f}|{estoque_f}\n")

        banco_dados.close()

        if not localizado:
            print("\n[!] Produto não localizado no banco de dados.")

        input("\nRetornar ao menu...")
        os.system("cls")

print("\nSistema finalizado.")