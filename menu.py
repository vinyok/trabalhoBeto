def exibir_menu():
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
    
    return input('Escolha uma opção: ')

escolha_user = exibir_menu ()
print('\nVocê escolheu a opção:', escolha_user)
    
        