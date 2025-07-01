eventos = {}

def adicionar_eventos(*args):
    nome, data, tema = args
    eventos.append({'nome': nome, 
                    'data': data, 
                    'tema': tema})
        # posso colocar pra mudar o nome do evento linkado aqui ou remover o evento existente