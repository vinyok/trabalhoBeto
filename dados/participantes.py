participantes = {}

def adicionar_participante(codigo_cpf, nome, tema_de_interesse):
    codigo_cpf = input('Digite seu cpf: ')
    nome = input('Digite seu primeiro e ultímo nome: ')
    tema_de_interesse = input('Digite um tema de interesse: ')
    novo_participante = {"código": codigo_cpf, "nome": nome, "tema de interesse": tema_de_interesse}
    participantes.append(novo_participante)

adicionar_participante ()