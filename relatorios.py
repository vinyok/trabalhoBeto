from util.limpar_tela import limpar_tela

def gerar_relatorios(participantes, eventos):
    if not eventos:
        print("Não há eventos para gerar relatório.")
        return
    print("\n===== Relatórios =====")
    print(f"Total de participantes cadastrados: {len(participantes)}")
    print(f"Total de eventos cadastrados: {len(eventos)}")
    
def contar_eventos_por_tema(eventos):
    if not eventos:
        print("Nenhum evento cadastrado.")
        return

    contagem = {}
    for evento in eventos:
        tema = evento["tema"]
        if tema in contagem:
            contagem[tema] += 1
        else:
            contagem[tema] = 1

    print("\nQuantidade de eventos por tema:")
    for tema, qtd in contagem.items():
        print(f"- {tema}: {qtd}")


def taxa_media_participacao_por_tema(eventos):
    if not eventos:
        print("Nenhum evento cadastrado.")
        return

    participacao_por_tema = {}
    eventos_por_tema = {}

    for evento in eventos:
        tema = evento["tema"]
        qtd_participantes = len(evento["participantes"])

        if tema in participacao_por_tema:
            participacao_por_tema[tema] += qtd_participantes
            eventos_por_tema[tema] += 1
        else:
            participacao_por_tema[tema] = qtd_participantes
            eventos_por_tema[tema] = 1

    print("\nTaxa média de participação por tema:")
    for tema in participacao_por_tema:
        media = participacao_por_tema[tema] / eventos_por_tema[tema]
        print(f"- {tema}: {media:.2f} participantes por evento")

def menu_relatorios(participantes, eventos):
    limpar_tela()
    gerar_relatorios(participantes, eventos)
    contar_eventos_por_tema(eventos)
    taxa_media_participacao_por_tema(eventos)
    input("\nPressione Enter para voltar ao menu principal...")