from participantes import adicionar_participante, buscar_participante, listar_participantes, remover_participante,atualizar_participante, listar_eventos_que_participante_esta_cadastrado, cadastrar_participante_em_evento

from eventos import adicionar_eventos, listar_eventos, remover_evento

from util.limpar_tela import limpar_tela

from relatorios import menu_relatorios

def exibir_menu():
    print("\n" + "="*40)
    print(' SISTEMA DE GERENCIAMENTO DE EVENTOS ')
    print("="*40)
        
    print('1. Adicionar novo participante')
    print('2. Adicionar novo evento')
    print('3. Cadastrar participante em evento')
    print('4. Listar participantes')
    print('5. Buscar participante')
    print('6. Listar eventos')
    print('7. Gerar relatórios e estatísticas')
    print('8. Remover participante')
    print('9. Atualizar informações de um participante')
    print('10. Remover evento')
    print('11. Listar eventos que o participante está cadastrado')
    print('0. Sair')
    
    print("="*40)

    entrada_user = input('Digite um número para escolher a opção: ')    
    if entrada_user.isdigit():
        return int(entrada_user)
    else:
        print('Entrada inválida. Digite um número.')
        return

def main():
    participantes = []
    eventos = []

    opcoes = {
        1: lambda: adicionar_participante(participantes),
        2: lambda: adicionar_eventos(eventos),
        3: lambda: cadastrar_participante_em_evento(participantes, eventos),
        4: lambda: listar_participantes(participantes),
        5: lambda: buscar_participante(participantes),
        6: lambda: listar_eventos(eventos),
        7: lambda: menu_relatorios(participantes, eventos),
        8: lambda: remover_participante(participantes),
        9: lambda: atualizar_participante(participantes),
        10: lambda: remover_evento(eventos),
        11: lambda: listar_eventos_que_participante_esta_cadastrado(participantes, eventos),
        0: lambda: print('Encerrando o sistema! ...'),
    }

    while True:
        limpar_tela()
        opcao = exibir_menu()

        if opcao == 0:
            print('Encerrando o sistema! ...')
            break

        if opcao in opcoes:
            limpar_tela()
            opcoes[opcao]()
            input("\nPressione Enter para continuar...")
        else:
            print('Opção inválida. Tente novamente! ')
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
    
        