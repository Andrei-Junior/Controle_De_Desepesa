# Dicionário para armazenar as despesas por mês
meses = {
    'Janeiro': [],
    'Fevereiro': [],
    'Março': [],
    'Abril': [],
    'Maio': [],
    'Junho': [],
    'Julho': [],
    'Agosto': [],
    'Setembro': [],
    'Outubro': [],
    'Novembro': [],
    'Dezembro': []
}

def menu():
    """
    Exibe o menu principal com as opções disponíveis para o usuário.
    """
    print("\n-------- MENU --------")
    print("1 - Adicionar uma despesa com descrição e valor.")
    print("2 - Atualizar uma despesa.")
    print("3 - Excluir uma despesa.")
    print("4 - Visualizar todas as despesas.")
    print("5 - Resumo das despesas de um mês específico.")
    print("6 - Visualizar o total de todas as despesas.")
    print("7 - Sair.")
    print("----------------------")

def adicionar_despesa():
    """
    Adiciona uma nova despesa a um mês específico.
    """
    try:
        valor = float(input("Digite o valor da despesa (R$): "))
    except ValueError:
        print("Valor inválido. Tente novamente.")
        return

    mes = input("Digite para qual mês (ex: Janeiro, Fevereiro, etc.): ").capitalize()

    if mes in meses:
        meses[mes].append(valor)
        print(f"Despesa de R$ {valor} adicionada ao mês de {mes}.")
    else:
        print("Mês inválido. Tente novamente.")

def atualizar_despesa():
    """
    Atualiza uma despesa existente em um mês específico.
    """
    mes = input("Digite o mês onde deseja atualizar a despesa: ").capitalize()

    if mes in meses and meses[mes]:
        print(f"Despesas atuais para o mês de {mes}: {meses[mes]}")
        try:
            indice = int(input("Digite o índice da despesa que deseja atualizar (começando de 0): "))
            nova_despesa = float(input("Digite o novo valor da despesa (R$): "))
            meses[mes][indice] = nova_despesa
            print(f"Despesa atualizada com sucesso! Lista atualizada: {meses[mes]}")
        except (ValueError, IndexError):
            print("Erro: Índice ou valor inválido.")
    else:
        print(f"Mês {mes} não encontrado ou não há despesas cadastradas.")

def excluir_despesa():
    """
    Exclui uma despesa de um mês específico.
    """
    mes = input("Em qual mês está a despesa que deseja excluir? ").capitalize()
    
    if mes in meses and meses[mes]:
        try:
            print(f"\nDespesas cadastradas em {mes}:")
            for despesa in meses[mes]:
                print(f"- R$ {despesa:.2f}")
            valor = float(input("Qual valor da despesa deseja excluir (R$)? "))
            if valor in meses[mes]:
                meses[mes].remove(valor)
                print(f"Despesa de R$ {valor} excluída do mês de {mes}.")
            else:
                print(f"Despesa de R$ {valor} não encontrada no mês de {mes}.")
        except ValueError:
            print("Valor inválido. Tente novamente.")
    else:
        print(f"Mês {mes} não encontrado ou não há despesas cadastradas.")

def visualizar_despesa():
    """
    Exibe todas as despesas cadastradas por mês.
    """
    print("\n------- VISUALIZAR DESPESAS -------")
    if not any(meses.values()):
        print("Não há despesas cadastradas.")
    else:
        for mes, despesas in meses.items():
            if despesas:
                print(f"{mes}: R$ " + " / R$ ".join(map(str, despesas)))
            else:
                print(f"{mes}: Nenhuma despesa cadastrada.")
    print("-----------------------------------")

def resumo_mes():
    """
    Exibe o resumo das despesas de um mês específico.
    """
    mes = input("Digite o mês que deseja ver o resumo: ").capitalize()
    
    if mes in meses:
        soma = sum(meses[mes])
        print(f"Total de despesas em {mes}: R$ {soma:.2f}")
    else:
        print(f"Mês {mes} não encontrado.")

def total_despesas():
    """
    Exibe o total de todas as despesas cadastradas no ano.
    """
    soma_total = sum(valor for lista in meses.values() for valor in lista)
    print(f"Total de todas as despesas no ano: R$ {soma_total:.2f}")

def sair():
    """
    Finaliza o programa.
    """
    print("Saindo... Até logo!")
    exit()

# Loop principal
while True:
    menu()  # Exibe o menu
    escolha = input("Escolha uma opção: ")
    
    # Executa a função conforme a escolha do usuário
    if escolha == "1":
        adicionar_despesa()
    elif escolha == "2":
        atualizar_despesa()
    elif escolha == "3":
        excluir_despesa()
    elif escolha == "4":
        visualizar_despesa()
    elif escolha == "5":
        resumo_mes()
    elif escolha == "6":
        total_despesas()
    elif escolha == "7":
        sair()
    else:
        print("Opção inválida. Tente novamente.")
