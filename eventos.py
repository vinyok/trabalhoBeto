def adicionar_eventos(eventos, *args, **kwargs):
    nome_evento = str(input('\nDigite o nome do evento: '))
    data_evento = str(input('\nDigite a data do evento(DD/MM/AAAA): '))
    tema_evento = str(input('\nDigite o tema do evento: '))
    senha_evento = str(input('\nDigite uma senha para editar ou remover futuramento o evento: '))
    novo_evento = {'nome': nome_evento,
                   'data': data_evento,
                   'tema': tema_evento,
                   'senha': senha_evento,
                   'participantes': [],}
    eventos.append(novo_evento)
    print(f'Evento {nome_evento} foi adicionado com sucesso! ')


def listar_eventos (eventos, *args, **kwargs):
    print('Lista de eventos disponíveis: ')
    if not eventos:
        print('Nenhum evento foi encontrado.')
    else:
        for evento in eventos:
            print(f"Nome do evento: {evento['nome']} - Data do evento: {evento['data']} - Tema do evento: {evento['tema']}")


def remover_evento(eventos):
    nome = input("Digite o nome do evento a ser removido: ")
    senha = input("Digite a senha do evento: ")

    for i, evento in enumerate(eventos):
        if evento["nome"] == nome and evento["senha"] == senha:
            del eventos[i]
            print(f"Evento '{nome}' removido com sucesso!")
            return
    print("Evento não encontrado ou senha incorreta.")
