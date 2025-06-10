def exibir_menu():
    while True:
        print("\n" + "="*40)
        print("  SISTEMA DE GERENCIAMENTO DE EVENTOS")
        print("="*40)
        
        print("1. Cadastrar novo evento")
        print("2. Cadastrar novo participante")
        print("3. Exibir eventos disponíveis")
        print("4. Buscar participante")
        print("5. Gerar relatórios")
        print("6. Exibir todos os participantes")
        print("7. Exibir eventos por tema")
        print("0. Sair do sistema")
        print("="*40)
        escolha = str (input('\nEscolha: ')).lower()
        return escolha


def executar_menu():
    opcoes = {
        "1": cadastrar_evento,
        "2": cadastrar_participante,
        "3": listar_eventos,
        "4": buscar_participante,
        "5": gerar_relatorios,
        "6": listar_todos_participantes,
        "7": listar_eventos_por_tema,
        "0": sair_sistema
    }
     
    while True:
        opcao = exibir_menu()
        acao = opcoes.get(opcao)

        if acao:
            acao()
        else:
            print("\nOpção inválida! Tente novamente.")

exibir_menu()