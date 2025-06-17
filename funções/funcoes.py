from dados import eventos, participantes
    
def adicionar_eventos(nome, tema, data):
    if nome not in eventos:
        eventos[nome] = {
            'data': data,
            'tema': tema,
            'participantes': [],
                        }
        print(f'O evento {nome} foi cadastrado com sucesso! ')
    else:
        print('Evento já existe. ')
        # posso colocar pra mudar o nome do evento linkado aqui ou remover o evento existente
        
def adicionar_participante_no_evento(nome_evento, codigo_cpf):
    if nome_evento not in eventos:
        print('Evento não encontrado. ')
    elif codigo_cpf not in participantes:
        print('Participante não encontrado.')
    elif codigo_cpf in eventos:
        print('Participante já inscrito no evento.')
        # conferir porque acho que está errado
    eventos[nome_evento] ['participantes'].append(codigo_cpf)
    print('Participante inscrito com sucesso! ')
    # tentar colocar o nome do participante aqui depois
    
def listar_eventos():
    if not eventos:
        print('Nenhum evento cadastrado. ')
    else:
        print(f'Todos os eventos cadastrados até o momento: {eventos}')
        
def procurar_participante(cpf):
    if cpf not in participantes:
        ('Participante não encontrado. ')
    

        